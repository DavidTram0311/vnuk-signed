from .custom_types import Gloss
from .common import load_spacy_model


LANGUAGE_MODELS_SPACY = {
    "de": "de_core_news_lg",
    "fr": "fr_core_news_lg",
    "it": "it_core_news_lg",
    # "en": "en_core_web_lg",
    "en": "en_core_web_sm",
}


def text_to_gloss(text: str, language: str, ignore_punctuation: bool = False) -> Gloss:
    """
    Convert text to glosses using spaCy lemmatization.
    """

    if language not in LANGUAGE_MODELS_SPACY:
        raise NotImplementedError("Don't know language '%s'." % language)

    model_name = LANGUAGE_MODELS_SPACY[language]

    # TODO: disable unnecessary components to make lemmatization faster
    # e.g. disable=("parser", "ner")
    spacy_model = load_spacy_model(model_name)
    doc = spacy_model(text)
    glosses = []  # type: Gloss

    for token in doc:
        if ignore_punctuation is True:
            if token.is_punct:
                continue

        gloss = (token.text, token.lemma_)
        glosses.append(gloss)

    return glosses
