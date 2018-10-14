import re
import requests
import urllib3
import os

with open('wikipedia_nc_counties.txt', 'r') as file:
    text = file.read()

counties = re.findall(r'(?<=Name=)[A-z]*', text)

if not os.path.exists('resources_by_nc_county'):
    os.makedirs('resources_by_nc_county')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for county in counties:
    url = 'http://www.ncworks.gov/admin/gsipub/htmlarea/uploads/CRAG/{}_County.pdf'.format(county)
    response = requests.get(url, verify=False)
    if (response.status_code >= 200 and response.status_code < 300):
        with open('resources_by_nc_county/{}_County.pdf'.format(county), 'wb') as pdf:
            pdf.write(response.content)
