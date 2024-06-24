from simplemma import simple_tokenizer
from simplemma import text_lemmatizer as simple_lemmatizer
from .custom_types import Gloss


def text_to_gloss(text: str, language: str) -> Gloss:

    words = [w.lower() for w in simple_tokenizer(text)]
    lemmas = [w.lower() for w in simple_lemmatizer(text, lang=language)]

    return list(zip(words, lemmas))
