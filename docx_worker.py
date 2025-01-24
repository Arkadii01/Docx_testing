from docx import Document
from docx.shared import Inches
import os

def docx_fixer(file=None):
    if file == None:
        doc = Document()
    else:
        doc = Document(f'docs_for_test//{file}')
    if file == None:
        pass
    else:
        doc.save(f'result//{file}')