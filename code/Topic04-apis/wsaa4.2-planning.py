# get planning applications
# Author: Andrew Beatty

import requests

#to get all the data from the url - takes time - sends back code 200 as ok
#url= "https://opendata.arcgis.com/datasets/8f69dffe26324ba3acc653cf6cb5cf8b_0.geojson"
#list_of_planning = requests.get(url)
#print (list_of_planning.status_code)


url= "https://opendata.arcgis.com/datasets/8f69dffe26324ba3acc653cf6cb5cf8b_0.geojson"
response = requests.get(url)
list_of_planning = response.json()
print (response.status_code)

print(list_of_planning["features"][0]["geometry"]["coordinates"])

# takes a long time to run
