import json
import os
from py_trans import PyTranslator
from py_trans import Async_PyTranslator

# Load the languages.json file
script_dir = os.path.dirname(os.path.abspath(__file__))
languages_file = os.path.join(script_dir, 'languages.json')
with open(languages_file, 'r') as f:
    languages = json.load(f)


def translate_text(text, target_language, translator_machine="google"):
    """
    Translate the given text to the target language using the specified translation service.

    :param text: The text to be translated.
    :param target_language: The target language to translate to.
    :param translator_machine: The translation service to use. Must be one of: "google", "translate_com", "my_memory", or "translate_dict".
    :return: The translated text.
    """
    # Check if the target_language is in the languages.json file
    if target_language not in languages.keys():
        print(f"Error: '{target_language}' is not a valid target language. Please choose from the following languages:")
        for code, lang in languages.items():
            print(f"- {code}: {lang}")
        return
    valid_options = ("google", "translate_com", "my_memory", "translate_dict")

    if translator_machine not in valid_options:
        raise ValueError(f"Invalid translator_machine option. Must be one of: {', '.join(valid_options)}.")

    translator = PyTranslator()
    translate_method = getattr(translator, translator_machine)
    translated_text = translate_method(text, target_language)
    return translated_text


# TODO: Implement Async_PyTranslator
