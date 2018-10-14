import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# functionality needed: create read update destroy

class Database:

    FIELDS = ['category', 'agency_name', 'address', 'phone', 'website', 'services']

    def __init__(self):
        self.cred = credentials.Certificate('/home/vishy/Git/basic-needs-app/bna/basic-needs-app-firebase-adminsdk-d4iio-09b7d4746f.json')
        self.default_app = firebase_admin.initialize_app(self.cred, {'databaseURL': 'https://basic-needs-app.firebaseio.com'})
        self.ref = db.reference('agencies')

    # creates a new entry. will overwrite an entry if it already exists
    def create(self, agency_ID=None, category=None, agency_name=None, address=None,
               phone=None, website=None, services=None):
        agency_ref = self.ref.child(agency_ID)
        agency_ref.set({

            'category': category,
            'agency_name': agency_name,
            'address': address,
            'phone': phone,
            'website': website,
            'services': services

        })

    def read(self, query):
        snapshot = self.ref.order_by_child('category').equal_to(query).get()
        return snapshot.values()

    # update an existing entry. pass in agency_ID and a dictionary of fields and values to update with
    def update(self, agency_ID, fields):
        agency_ref = self.ref.child(agency_ID)
        for field in fields:
            if field in self.FIELDS:
                agency_ref.update({field: fields[field]})

    def destroy(self, agency_ID):
        agency_ref = self.ref.child(agency_ID)
        agency_ref.delete()


# -- DEBUGGING ONLY --


# ref = db.reference('example')
#
# example_ref = ref.child('this_is_a_test')
# example_ref.set({
#     'id1': {
#         'field1': 'field2 is true',
#         'field2': True
#     },
#     'id2': {
#         'field1': 'field2 is false',
#         'field2': False
#     }
# })

# example.create(
#             'nc-childcare-network',
#             'Childcare/Youth Services',
#             'NC Childcare Network',
#             '319 Chapanoke Road, Suite 120, Raleigh, N. C. 27603',
#             '(800) 859-0829',
#             'http://www.ncchildcare.net',
#             'Service(s) Offered: Regulates the health, safety, and well-being of children in out-of-home care; Provides support and quality control services to child care providers'
#             )

# example.update('nc-childcare-network', {'address': '2201 Mail Service Center Raleigh, N. C. 27699-2201'})

# entry = example.read('nc-childcare-network')
# print(entry)

# example.destroy('nc-childcare-network')
