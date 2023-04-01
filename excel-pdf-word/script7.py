import docx

def getText(filename):
    doc = docx.Document(filename)
    
    fullText = []
    
    for para in doc.paragraphs:
        fullText.append(para.text)
    
    return '\n'.join(fullText)

print(getText('F:\\python_programs\\automation\\excel-pdf-word\\demo.docx'))        