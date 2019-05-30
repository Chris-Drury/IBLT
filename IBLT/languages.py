"""
This file is responsable for returning the language
in the format that is used by googletrans.

dependancies:
googletrans
"""

from googletrans import LANGUAGES


def get_lang_code(lang: str):
    # setup a dictionary to change requested languagues into langcodes
    Langcodes = dict(map(reversed, LANGUAGES.items()))
    # return the code of the requested language
    return(Langcodes[lang])

