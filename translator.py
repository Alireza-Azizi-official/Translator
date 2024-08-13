import sys
from deep_translator import GoogleTranslator

sys.stdout.reconfigure(encoding = 'utf-8')

def translate(text, language):
    translator = GoogleTranslator(source = 'auto', target = language)
    translator = translator.translate(text)
    
    return translator

txt_input = 'hello to you'
translated = translate(txt_input, 'fa')
