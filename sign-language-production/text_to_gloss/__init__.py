import importlib


def text2gloss_module(glosser: str):
    """
    Import and return the glosser module of selection
    :param glosser: select a text to gloss module in ['simple', 'spacylemma', 'rules', 'nmt' (upcoming), 'seq2seq_attention']
    :return: text to gloss function that is ready to be used with func(text: str, language: str) -> Gloss
    """
    try:
        module = importlib.import_module(f"text_to_gloss.{glosser}")
        func = getattr(module, "text_to_gloss")
    except ModuleNotFoundError:
        raise ValueError(f"Glosser {glosser} not found. "
                         f"Please choose: ['simple', 'spacylemma', 'rules', 'nmt' (upcoming), 'seq2seq_attention']")
    except AttributeError:
        raise ValueError(f"The module {glosser} does not have a 'text_to_gloss' function.")

    return func
