"""
    This app will allow users to get information from a specific realestate website
    and combine the information into a single file
"""
import pandas, requests, time
from bs4 import BeautifulSoup

""" Get the number of pages/object on the site by using the url """
# Connect to website
base_url = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'
r = requests.get(base_url,
 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
# Get content
c = r.content
# Create the parser that will read through the data
parser = BeautifulSoup(c, 'html.parser')
# get number of of items on the site
itemsPerPage = int(parser.find('div', {'class' : 'PaginationLimit'}).find('div', {'class' : 'selector smallSelector'})
 .find('span').text)
itemCount = (len(parser.find_all('div', {'class' : 'PagerFull'}))+1) * itemsPerPage

# Store data in a list to be added to a data frame
allOffers = []

""" loop throough all of the pages and get data"""
# loop through all pages
for num in range(0, itemCount, itemsPerPage):
    print(base_url + 't=0&s={}'.format(str(num)))
    r = requests.get(base_url + 't=0&s={}.html'.format(str(num)), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    parser = BeautifulSoup(c, 'html.parser')

    # Get info for each item in the given list on the website
    listingsAll = parser.find_all('div', {'class' : 'propertyRow'})

    # A list to hold listing object dict - no longer needed
    #offers = []

    # Go to each listing element and get the info from it
    for lot in listingsAll:
        currentLotInfoDict = dict()
        # Get the price
        price = lot.find('h4', {'class' : 'propPrice'}).text.replace('\n', '').replace(' ', '')
        currentLotInfoDict['Price'] = price
        # Get the address lines - two lines so  need to take into account
        address1 = lot.find_all('span', {'class' : 'propAddressCollapse'})[0].text
        address2 = lot.find_all('span', {'class' : 'propAddressCollapse'})[1].text# will get a list of 2 items
        currentLotInfoDict['Address'] = address1
        currentLotInfoDict['Location'] = address2
        # get bed count
        try:
            beds = lot.find('span', {'class' : 'infoBed'}).find('b').text
        except:
            beds = None
        currentLotInfoDict['Beds'] = beds
        # get full bath count
        try:
            bathsFull = lot.find('span', {'class' : 'infoValueFullBath'}).find('b').text
        except:
            bathsFull = None
        currentLotInfoDict['Full Baths'] = bathsFull
        # get half bath count
        try:
            bathsHalf = lot.find('span', {'class' : 'infoValueHalfBath'}).find('b').text
        except:
            bathsHalf = None
        currentLotInfoDict['Half Baths'] = bathsHalf
        # get sq ft
        try:
            sqFt = lot.find('span', {'class' : 'infoSqFt'}).find('b').text
        except:
            sqFt = None
        currentLotInfoDict['Sq. Ft'] = sqFt
        # get property description
        try:
            description = lot.find('div', {'class' : 'propertyDescCollapse'}).text[1:-12]
        except:
            description = None
        currentLotInfoDict['Description'] = description

        lotSize = None
        otherFeatures = {}
        currentLotInfoDict['Lot Size'] = None
        # loop through all the features and find lot size, save the rest of the features
        for feature in lot.find_all('div', {'class' : 'columnGroup'}):
            # use zip command to travers two lists at the same time
            # Since every feature name will have a description added, can travers without worrying about getting different len lists
            for featureGroup, featureName in zip(feature.find_all('span', {'class' : 'featureGroup'}),
            feature.find_all('span', {'class' : 'featureName'})):
                # will need to add to object before writting to file
                # get lot size
                if 'Lot Size' in featureGroup.text:
                    lotSize = featureName.text
                    currentLotInfoDict['Lot Size'] = lotSize
                else:
                    otherFeatures['{}'.format(featureGroup.text.replace('\xa0', ''))] = featureName.text
        
        # Add other features to dict
        currentLotInfoDict["Features"] = otherFeatures
        # Add to offers list to later be added to a data frame
        allOffers.append(currentLotInfoDict)

        '''
        # Print for testing
        print(price)
        print(address1 + '\n' + address2)
        print(beds)
        print(bathsFull)
        print(bathsHalf)
        print(sqFt)
        print(description)
        print(lotSize)
        print(otherFeatures)
        time.sleep(1)
        '''

# Write the offers list to a csv file file
df = pandas.DataFrame(allOffers)
"""
    when having multiple lists, its better to append the lists and then add it to the data frame
    rather than trying to create a data frame and later add to it
"""
df.to_csv('available_listings.csv')
    
