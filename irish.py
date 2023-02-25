from googletrans import Translator

translator = Translator()

words_to_translate = ["hello", "goodbye", "endometriosis"]

for word in words_to_translate:
    translated = translator.translate(word, dest='ga')
    print(f"{word} in Irish is {translated.text}")
