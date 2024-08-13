import fitz
from deep_translator import GoogleTranslator

def extract_text_from_pdf(pdf_path):
    text = ''
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def translate(text, language):
    translator = GoogleTranslator(source = 'auto', target = language)
    translated = translator.translate(text)
    return translated

def write_to_file(translated_text, filename, words_per_line = 10):
    words = translated_text.split()
    with open(filename, 'w', encoding = 'utf-8') as file :
        for i in range(0, len(words), words_per_line):
            line_words = words[i:i + words_per_line]  
            file.write(' '.join(line_words) + '\n')         
                      
pdf_path = r'D:\10_PYTHON PROJECTS\Translator\As Michael Harvey writes.pdf'
txt_input = extract_text_from_pdf(pdf_path)
translated = translate(txt_input, 'fa')
file_name = 'translated_file.txt'
write_to_file(translated, file_name)