import PyPDF2

import os

os.chdir('F:\\python_programs\\automation\\excel-pdf-word')

pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfReader(pdfFile)

# page = reader.pages[0]

# print(page.extract_text())

for pageNum in range(len(reader.pages)):
    print(reader.pages[pageNum].extract_text())
