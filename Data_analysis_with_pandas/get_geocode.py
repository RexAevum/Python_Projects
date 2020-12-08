import pandas
from geopy.geocoders import ArcGIS

nom = ArcGIS()

# get the info from a db
df = pandas.read_csv("data\supermarkets.csv")

# Create/update a new column that will hold all of the data the geocoder needs to find location
df["Full_Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

# Create a new column that will store the location object that is returned from the geocoder
df["Location"] = df["Full_Address"].apply(nom.geocode)

#get location
print(df)

# Once you have the location create 2 new columns that store latitude and longitude
df["Latitude"] = df["Location"].apply(lambda x: x.latitude if x != None else None) # for each x, apply the .latitude value
# The if/else is to make sure you dont get an error 

# Do the same for longitude
df["Longitude"] = df["Location"].apply(lambda x: x.longitude if x != None else None)