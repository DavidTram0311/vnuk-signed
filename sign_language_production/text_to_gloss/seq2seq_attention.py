import urllib.request
import os
import torch
import datasets
import torchtext;
torchtext.disable_torchtext_deprecation_warning()
from torchtext import vocab
from .models import *
from .support_funcs import *
from .custom_types import Gloss
from .spacylemma import LANGUAGE_MODELS_SPACY
from .common import load_spacy_model


def load_vocab(vocab_path):
    vocab_data = torch.load(vocab_path)
    return vocab_data['en_vocab'], vocab_data['de_vocab']


def save_vocab(en_vocab, de_vocab, vocab_path):
    torch.save({'en_vocab': en_vocab, 'de_vocab': de_vocab}, vocab_path)


def build_and_save_vocab(train_data, min_freq, special_tokens, vocab_path):
    en_vocab = vocab.build_vocab_from_iterator(train_data["en_tokens"], min_freq=min_freq, specials=special_tokens)
    de_vocab = vocab.build_vocab_from_iterator(train_data["de_tokens"], min_freq=min_freq, specials=special_tokens)

    assert en_vocab["<unk>"] == de_vocab["<unk>"]
    assert en_vocab["<pad>"] == de_vocab["<pad>"]

    en_vocab.set_default_index(en_vocab["<unk>"])
    de_vocab.set_default_index(en_vocab["<unk>"])

    save_vocab(en_vocab, de_vocab, vocab_path)
    return en_vocab, de_vocab


def load_model(model_path,
               input_dim, output_dim,
               encoder_embedding_dim, decoder_embedding_dim,
               encoder_hidden_dim, decoder_hidden_dim,
               encoder_dropout, decoder_dropout,
               device):
    attention = Attention(encoder_hidden_dim, decoder_hidden_dim)
    encoder = Encoder(input_dim, encoder_embedding_dim, encoder_hidden_dim, decoder_hidden_dim, encoder_dropout)
    decoder = Decoder(output_dim, decoder_embedding_dim, encoder_hidden_dim, decoder_hidden_dim, decoder_dropout,
                      attention)
    model = Seq2Seq(encoder, decoder, device).to(device)
    model.load_state_dict(torch.load(model_path))
    return model


def prepare_data():
    dataset_ASL = datasets.load_dataset("aslg_pc12")
    dataset_ASL = dataset_ASL.rename_columns({'gloss': 'en', 'text': 'de'})
    dataset_ASL = strip_bom_and_newline(dataset_ASL)
    dataset = split_dataset(dataset_ASL["train"])
    return dataset["train"]


def tokenize_data(train_data, en_nlp, de_nlp,
                  max_length=1_000, lower=True, sos_token="<sos>", eos_token="<eos>"):
    fn_kwargs = {
        "en_nlp": en_nlp,
        "de_nlp": de_nlp,
        "max_length": max_length,
        "lower": lower,
        "sos_token": sos_token,
        "eos_token": eos_token,
    }
    return train_data.map(tokenize_example, fn_kwargs=fn_kwargs)


def text_to_gloss(text: str, language: str = "en") -> Gloss:
    # Define paths for saved components
    # Define the base directory as the directory of this script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Define paths for saved components
    vocab_filename = 'aslg-pc12-vocab.pt'
    model_filename = 'text2gloss-aslg_pc12-model-03-batch32.pt'
    VOCAB_PATH = os.path.join(BASE_DIR, vocab_filename)
    MODEL_PATH = os.path.join(BASE_DIR, model_filename)

    # Check if vocab and model weight files exist, download if not
    if not os.path.exists(VOCAB_PATH):
        print(f'Vocab file not found. Downloading vocab file.')
        vocab_url = "https://drive.usercontent.google.com/download?id=1jebwdnDyA4-9s3mCDWdO5wuNcVCChglz&export=download"
        urllib.request.urlretrieve(vocab_url, VOCAB_PATH)
        print(f'Vocab file downloaded to {VOCAB_PATH}')
    else:
        print(f'Vocab file found. Loading vocab from file.')

    if not os.path.exists(MODEL_PATH):
        print(f'Model file not found. Downloading model file.')
        model_url = "https://drive.usercontent.google.com/download?id=1VVTfDcO65o_ZPteybCzXh4XCYV7wEgC1&export=download"
        urllib.request.urlretrieve(model_url, MODEL_PATH)
        print(f'Model file downloaded to {MODEL_PATH}')
    else:
        print(f'Model file found. Loading model from file.')

    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f'Device using: {DEVICE}')

    # define tokenizer: English for both spoken English and ASL gloss
    # "en_" for ASL gloss; "de_" for spoken English
    # spacy_model = 'en_core_web_sm'
    spacy_model = LANGUAGE_MODELS_SPACY[language]
    # TODO: disable unnecessary components to speed-up the lemmatizer like this:
    # spacy_model = load_spacy_model(spacy_model, disable=("parser", "ner"))
    en_nlp = load_spacy_model(spacy_model)
    de_nlp = load_spacy_model(spacy_model)

    # prepare vocab
    if not os.path.exists(VOCAB_PATH):
        print(f'Vocab file not found. Building vocab from data.')
        train_data = prepare_data()
        train_data = tokenize_data(train_data, en_nlp, de_nlp)
        en_vocab, de_vocab = build_and_save_vocab(train_data,
                                                  min_freq=2,
                                                  special_tokens=["<unk>", "<pad>", "<sos>", "<eos>"],
                                                  vocab_path=VOCAB_PATH)
    else:
        print(f'Vocab file found. Loading vocab from file.')
        en_vocab, de_vocab = load_vocab(VOCAB_PATH)

    # load model
    input_dim = len(de_vocab)
    output_dim = len(en_vocab)

    model = load_model(model_path=MODEL_PATH,
                       input_dim=input_dim, output_dim=output_dim,
                       encoder_embedding_dim=256, decoder_embedding_dim=256,
                       encoder_hidden_dim=512, decoder_hidden_dim=512,
                       encoder_dropout=0.5, decoder_dropout=0.5,
                       device=DEVICE)

    # Translate spoken English to ASL gloss
    translation, sentence_tokens, attention = translate_sentence(
        text, model, en_nlp, de_nlp, en_vocab, de_vocab,
        lower=True, sos_token="<sos>", eos_token="<eos>", device=DEVICE
    )
    # print("Predicted gloss:\n {}".format(translation))
    return list(zip(sentence_tokens, translation))


if __name__ == "__main__":
    text_to_gloss()
