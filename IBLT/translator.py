"""
This file is responsable for translating
the isolated text from text_isolator.py.

dependancies:
googletrans
"""

from googletrans import Translator


def text_translator(text: str, lang: str):
    """translate the passed text into the passed language

    Keyword arguments:
    text -- the text to be translated
    lang -- the language to be translated to -- in langcode form
    """

    # setup the translator
    translator = Translator()

    # translate the text to the selected language
    translated = translator.translate(text, dest=lang)

    # print(translated)
    #  -> "Translated(src=zh-CN, dest=en, text=Hello there, 
    #                   pronunciation=None, extra_data="{'translat...")"
    # print(translated.text)
    #  -> "Hello there"
    # print(translated)
    #  -> "Translated(src=en, dest=fr, text=Bonjour, 
    #                   pronunciation=Bonjour, extra_data="{'translat...")"

    return translated.text
