
# importing required modules
import PyPDF2
import re
import db
import random

class Category:

    def __init__(self, name, raw_data):
        self.name = name
        self.raw_data = raw_data
        self.agencies = []

class Agency:
    def __init__(self, name):
        self.name = name
        self.address = ''
        self.phone = ''
        self.website = ''
        self.desc = ''

# creating a pdf file object
pdfFileObj = open('../Wake_County_resources_2017.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

numPages = pdfReader.numPages
pdfText = ""

for i in range(1, numPages):
    # creating a page object
    pageObj = pdfReader.getPage(i)

    # extracting text from page
    pdfText += pageObj.extractText()


# Taking out the header
pdfText = pdfText.split("Childcare/Youth Services\n")[1]

# Childcare/Youth Services
childcare = pdfText.split("Clothing\n")[0]
pdfText = pdfText.split("Clothing\n")[1] # rest of text

# Clothing
clothing = pdfText.split("Education/Training\n")[0]
pdfText = pdfText.split("Education/Training\n")[1] # rest of text

# Education/Training
education = pdfText.split("Employment\n")[0]
pdfText = pdfText.split("Employment\n")[1] # rest of text

# Employment
employment = pdfText.split("Financial Assistance\n")[0]
pdfText = pdfText.split("Financial Assistance\n")[1] # rest of text

# Financial Assistance
financial = pdfText.split("Food\n/Nutrition Assistance\n")[0]
pdfText = pdfText.split("Food\n/Nutrition Assistance\n")[1] # rest of text

# Food/Nutrition Assistance
food = pdfText.split("Handicapped/Disabled\n Services\n")[0]
pdfText = pdfText.split("Handicapped/Disabled\n Services\n")[1] # rest of text

# Handicapped/Disabled Services
handicapped = pdfText.split("Housing/Home Ownership\n")[0]
pdfText = pdfText.split("Housing/Home Ownership\n")[1] # rest of text

# Housing/Home Ownership
housing = pdfText.split("Legal Aid \n")[0]
pdfText = pdfText.split("Legal Aid \n")[1] # rest of text
# print(housing.encode('cp1252', errors='replace'))

# Legal Aid
legal = pdfText.split("Medical Care\n")[0]
pdfText = pdfText.split("Medical Care\n")[1] # rest of text

# Medical Care
medical = pdfText.split("Starting a Small Business\n")[0]
pdfText = pdfText.split("Starting a Small Business\n")[1] # rest of text

# Starting a Small Business
business = pdfText.split("Transportation\n")[0]
pdfText = pdfText.split("Transportation\n")[1] # rest of text

# Transportation
transportation = pdfText.split("Miscellaneous/Other Services \n")[0]
pdfText = pdfText.split("Miscellaneous/Other Services \n")[1] # rest of text

# Miscellaneous/Other Services
miscellaneous = pdfText
# print(miscellaneous)

categories = [Category('childcare',childcare),
              Category('clothing', clothing),
              Category('education', education),
              Category('employment',employment),
              Category('financial', financial),
              Category('food', food),
              Category('handicapped', handicapped),
              Category('housing', housing),
              Category('legal',legal),
              Category('medical', medical),
              Category('business', business),
              Category('transportation', transportation),
              Category('miscellaneous', miscellaneous)
             ]

for cat in categories:
    dat = ' '.join(cat.raw_data.split())
    agencies = re.findall(r'(?<=ress:)[^:]+',dat)
    cat.agencies = [Agency(' '.join(ag.split()[:-1])) for ag in agencies]

d = db.Database()

cnt = 0
for cat in categories:
    print cat.name
    for ag in cat.agencies:
            cnt += 1
            if(cnt > 11):
                print cat.name+'_'+ ag.name.split()[0]
                try:
                    d.create(agency_ID= cat.name+'_'+ag.name.split()[0], category=cat.name, address=ag.name)
                except:
                    d.create(agency_ID= cat.name+'_'+str(random.randrange(256)), category=cat.name, address=ag.name)




# closing the pdf file object
pdfFileObj.close()
