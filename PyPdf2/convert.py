import PyPDF2


pdfFile = '/home/wargun/Documents/other/primary.pdf'
pdfRead = PyPDF2.PdfFileReader(pdfFile)
print(pdfRead.getNumPages())
print(pdfRead.getPage(2).extractText())
str = ""
for i in range(1, 234):
    str += pdfRead.getPage(i).extractText()
with open('text.csv', 'w', encoding='utf-8') as f:
    f.write(str)
