"""
This file is responsable for translating
the isolated text from text_isolator.py.

dependancies:
googletrans
"""

from googletrans import Translator


def text_translator(text: str):
    """translate the passed text

    Keyword arguments:
    text -- the text to be translated
    """

    # setup the translator?
    translator = Translator()

    translated = translator.translate('你好')
    # print(translated)
    #  -> "Translated(src=zh-CN, dest=en, text=Hello there, 
    #                   pronunciation=None, extra_data="{'translat...")"
    # print(translated.text)
    #  -> "Hello there"

    translated = translator.translate(translated.text, dest='fr')
    # print(translated)
    #  -> "Translated(src=en, dest=fr, text=Bonjour, 
    #                   pronunciation=Bonjour, extra_data="{'translat...")"

    return "translated text"
