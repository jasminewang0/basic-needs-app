
# importing required modules
import PyPDF2
import csv
import os

# potential regex patterns

# (?<=  )[A-Z][a-z\n ]*/*[A-z\n ]+(?= Agency Name)
# (NC |assistance *)([A-Z][A-z/ ]+)(?=Agency Name)
# ([A-Z ]*)([A-Z][A-z/ ]+)(?=Agency Name)

headertable = [[], [], [],
               [], [], [],
               [], [], [],
               [], [], []]

pdffileobj = open('resources_by_nc_county/Durham_County.pdf', 'rb')
pdfr = PyPDF2.PdfFileReader(pdffileobj)
text = ""

numPages = pdfr.numPages

for i in range(1, numPages):
    pageObj = pdfr.getPage(i)
    text += pageObj.extractText().replace('\u02c7', '').replace('\n', '').replace('details.', 'details').replace('details', 'details.')

pdffileobj.close()

print(text)

# for pdf in os.listdir('resources_by_nc_county')
#
#         #
#
#         # creating a pdf file object
#         pdfFileObj = open(pdf, 'rb')
#
#         # creating a pdf reader object
#         pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
#         numPages = pdfReader.numPages
#         pdfText = ""
#
#         for i in range(1, numPages):
#             # creating a page object
#             pageObj = pdfReader.getPage(i)
#
#             # extracting text from page
#             pdfText += pageObj.extractText()
#
#         # Taking out the header
#         pdfText = pdfText.split("Childcare/Youth Services\n")[1]
#
#         # Childcare/Youth Services
#         childcare = pdfText.split("Clothing\n")[0]
#         pdfText = pdfText.split("Clothing\n")[1] # rest of text
#
#         # Clothing
#         clothing = pdfText.split("Education/Training\n")[0]
#         pdfText = pdfText.split("Education/Training\n")[1] # rest of text
#
#         # Education/Training
#         education = pdfText.split("Employment\n")[0]
#         pdfText = pdfText.split("Employment\n")[1] # rest of text
#
#         # Employment
#         employment = pdfText.split("Financial Assistance\n")[0]
#         pdfText = pdfText.split("Financial Assistance\n")[1] # rest of text
#
#         # Financial Assistance
#         financial = pdfText.split("Food\n/Nutrition Assistance\n")[0]
#         pdfText = pdfText.split("Food\n/Nutrition Assistance\n")[1] # rest of text
#
#         # Food/Nutrition Assistance
#         food = pdfText.split("Handicapped/Disabled\n Services\n")[0]
#         pdfText = pdfText.split("Handicapped/Disabled\n Services\n")[1] # rest of text
#
#         # Handicapped/Disabled Services
#         handicapped = pdfText.split("Housing/Home Ownership\n")[0]
#         pdfText = pdfText.split("Housing/Home Ownership\n")[1] # rest of text
#
#         # Housing/Home Ownership
#         housing = pdfText.split("Legal Aid \n")[0]
#         pdfText = pdfText.split("Legal Aid \n")[1] # rest of text
#         # print(housing.encode('cp1252', errors='replace'))
#
#         # Legal Aid
#         legal = pdfText.split("Medical Care\n")[0]
#         pdfText = pdfText.split("Medical Care\n")[1] # rest of text
#
#         # Medical Care
#         medical = pdfText.split("Starting a Small Business\n")[0]
#         pdfText = pdfText.split("Starting a Small Business\n")[1] # rest of text
#
#         # Starting a Small Business
#         business = pdfText.split("Transportation\n")[0]
#         pdfText = pdfText.split("Transportation\n")[1] # rest of text
#
#         # Transportation
#         transportation = pdfText.split("Miscellaneous/Other Services \n")[0]
#         pdfText = pdfText.split("Miscellaneous/Other Services \n")[1] # rest of text
#
#         # Miscellaneous/Other Services
#         miscellaneous = pdfText
#         # print(miscellaneous)
#
#         categories = [childcare, clothing, education, employment, financial,
#                       food, handicapped, housing, legal, medical, business,
#                       transportation]
#
#         for category in categories:
#             print(category)
#
#         # closing the pdf file object
#         pdfFileObj.close()
