import PyPDF2
from PyPDF2 import PdfFileReader

# Extracting text from PDF file
# Please note that the below process doesn’t work for scanned PDFs.

# Creating a pdf file object
pdf = open('data/file.pdf', 'rb') ## for reading pdf binary mode needed

# Creating pdf reader object
pdf_reader = PdfFileReader(pdf)

# Checking number of pages in a pdf file
print(pdf_reader.numPages)

# creating a page object
page = pdf_reader.getPage(0)

# finally extracting text from the page
print(page.extractText())

pdf.close()

# print()
# or Same process using context preprocessor

with open("data/file.pdf", 'rb') as pdf:  ## for reading pdf binary mode needed
    # Creating pdf reader object
    pdf_reader = PdfFileReader(pdf)

    # Checking number of pages in a pdf file
    print(pdf_reader.numPages)

    # creating a page object
    page = pdf_reader.getPage(0)

    # finally extracting text from the page
    print(page.extractText())
