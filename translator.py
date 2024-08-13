import sys
from deep_translator import GoogleTranslator

def translate(text, language):
    translator = GoogleTranslator(source = 'auto', target = language)
    translated = translator.translate(text)
    return translated 

def write_words_to_file(translated_text, filename):
    words = translated_text.split()
    with open(filename, 'w', encoding= 'utf-8') as file: 
        for word in words:
            file.write(word + '\n')
            
txt_input = 'hello to you'
translated = translate(txt_input, 'fa')


filename = 'translated_words.txt'
write_words_to_file(translated, filename)