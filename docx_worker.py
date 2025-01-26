from docx import Document
from docx.shared import Inches
import json
import os

def docx_fixer():
    os.chdir('data')
    with open('data.json', 'r', encoding='utf-8') as file:
        text = ''.join(file.readlines())[1:]
        data = json.loads(text)
    os.chdir('../docs_for_test')
    if file == None:
        doc = Document()
    else:
        doc = Document(f'docs_for_test//{file}')
    os.chdir('../result')
    if file == None:
        pass
    else:
        doc.save(f'result//{file}')
    os.chdir('..')