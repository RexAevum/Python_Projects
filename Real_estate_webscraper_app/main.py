"""
    This app will allow users to get information from a specific realestate website
    and combine the information into a single file
"""
import pandas, requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/",
 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
# Get content
c = r.content
# Create the parser that will read through the data
parser = BeautifulSoup(c, 'html.parser')
# Get info for each item in the given list on the website
listingsAll = parser.find_all('div', {'class' : 'propertyRow'})

# Go to each listing element and get the info from it
for lot in listingsAll:
    # Get the price
    price = lot.find('h4', {'class' : 'propPrice'}).text.replace('\n', '').replace(' ', '')
    print(price)
    # Get the address lines - two lines so  need to take into account
    address = lot.find_all('span', {'class' : 'propAddressCollapse'})[0].text +', ' + lot.find_all('span', {'class' : 'propAddressCollapse'})[1].text# will get a list of 2 items
    print(address)
    # get bed count
    try:
        beds = lot.find('span', {'class' : 'infoBed'}).find('b').text
    except:
        beds = None
    # get full bath count
    try:
        bathsFull = lot.find('span', {'class' : 'infoValueFullBath'}).find('b').text
    except:
        bathsFull = None
    # get half bath count
    try:
        bathsHalf = lot.find('span', {'class' : 'infoValueHalfBath'}).find('b').text
    except:
        bathsHalf = None
    # get sq ft
    try:
        sqFt = lot.find('span', {'class' : 'infoSqFt'}).find('b').text
    except:
        sqFt = None
    # get property description
    description = lot.find('div', {'class' : 'propertyDescCollapse'}).text[:-12]

    # Print for testing
    print(beds)
    print(bathsFull)
    print(bathsHalf)
    print(sqFt)
    print(description)
