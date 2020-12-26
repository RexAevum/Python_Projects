import requests
from bs4 import BeautifulSoup

# load the web page
r = requests.get("http://www.pyclass.com/example.html",
 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
# ge the content of the web page
contentOfWebPage = r.content
# Proces text
soup = BeautifulSoup(contentOfWebPage, 'html.parser')
# .find_all(sections of code you are looking for, {section type : specific type/class name}) - get all sectiopns of html that you specified
all = soup.find_all('div', {'class' : 'cities'})
# .find_all(sections of code you are looking for, {section type : specific type/class name})[0] - get first element
soup.find_all('div', {'class' : 'cities'})[0]

# Repeat the find_all() to further filter through the file and get the city name
city = all[0].find_all('h2')[0].text

# to get multiple items need to loop through
for city in all:
    print(city.find_all('h2')[0].text)
    print(city.find_all('p')[0].text)
