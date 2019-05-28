from googletrans import Translator

translator = Translator()

translated = translator.translate('你好')
#print(translated)
# -> "Translated(src=zh-CN, dest=en, text=Hello there, pronunciation=None, extra_data="{'translat...")"
#print(translated.text)
# -> "Hello there"

translated = translator.translate(translated.text, dest='fr')
#print(translated)
# -> "Translated(src=en, dest=fr, text=Bonjour, pronunciation=Bonjour, extra_data="{'translat...")"