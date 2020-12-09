"""
The given application will allow users to view an online map of the worlds and it will also show the following inf:
1) Will show the locations of volcanos 
2) Will show the population braket of all the countries

Tech used:
- Folium
"""
import folium
import pandas
from typing import final # for final

# create a map 
# Would need to get locations from DB
# map coordionates [-90 to 90, -180 to 180]
map = folium.Map(location=[39.708424, -105.077659], zoom_start=6, tiles="Stamen Terrain") # The location is coordionates

# import the locations that i want to display on the map using pandas
filePath = r"data\Volcanoes.txt"
dfVolcanoes = pandas.read_csv(filePath)

# Get the information we need from the data frame
lat = dfVolcanoes["LAT"]
lon = dfVolcanoes["LON"]
names = dfVolcanoes["NAME"]
elevations = dfVolcanoes["ELEV"]

# To add more interaction to the app, can make the popup be a link that will perform a search on google once presses
htmlPopUp = """<h4>Volcano:<br></h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Elevation: %s m
"""

# create a function that gets an elevation, then it returns a color name for the markers
low_vol: final = 1000
med_vol: final = 2000
high_vol: final = 3000
def pickColor(elevation):
    if elevation < low_vol:
        return 'blue'
    elif low_vol <= elevation < med_vol:
        return 'green'
    elif med_vol <= elevation < high_vol:
        return 'orange'
    else:
        return 'red'

# The loop through all of the items in data frame of volcanoes
featureGroupOfVolcanoes = folium.FeatureGroup(name="Volcanoes USA")
for lat, lon, name, el in zip(lat, lon, names, elevations): # The zip() function allows you to travers two seperate lists at the same time
    # A custom popup, rather than the default for more customazation and can use html
    iframe = folium.IFrame(html=htmlPopUp % (name, name, el), width=200, height=130)
    featureGroupOfVolcanoes.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iframe), tooltip=name, icon=folium.Icon(icon='star', color=pickColor(el))))
    
    """
    # Can customize the marker icon by using one of the other functions in the folium
    featureGroupOfVolcanoes.add_child(folium.CircleMarker(location=[lat, lon], radius=6, popup=folium.Popup(iframe), 
    fill_color = pickColor(el), color='grey', fill_opacity=1.0)) # Set the collor of the circles based on the created method pickColor(elevation)
    
    """

# Create a seperate Feature Group for population, so that later you can control each layer on its own
featureGroupOfPopulation = folium.FeatureGroup(name="Population")

# To add a polygon layer to the map
fileJson = r"data\world.json"
# due to the specifics of folium need to add the encoding='utf-8-sig' and since it requests a string instead of a file pointer need
# to add .read() at the end of the method call to get string --> folium.GeoJson().read()
featureGroupOfPopulation.add_child(folium.GeoJson(data=open(fileJson, 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor' : 'blue' if x['properties']['POP2005'] < 1000000 else ('green' if 1000000 <= x['properties']['POP2005'] < 10000000 
else 'red')})) 
#FIXME - Look up more info on lambda functions

# add the feature group to
map.add_child(featureGroupOfVolcanoes)
map.add_child(featureGroupOfPopulation)
# To add layer control, will need to use .add_child() method
map.add_child(folium.LayerControl(position='topright', collapse=False))

"""
# To add markers need to use the .add_child() and the child will be a .Marker from folium
map.add_child(folium.Marker(location=[25, -80], popup="I'm here", icon=folium.Icon(color='red')))

# To make the process cleaner you I can use folium.FeatureGroup that can hold many items to be added all at once later on
# Will help if you want to add layers to the map
fg = folium.FeatureGroup(name='Test map')
fg.add_child(folium.Marker(location=[20, -75], popup="I'm here too", icon=folium.Icon(color='green')))
map.add_child(fg)
"""

# Create the map and transfer it to a file - the last step
map.save(r"Maps\Volcano_And_Population_Map_v0.9.html")

