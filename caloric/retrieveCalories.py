
import requests
import json

#lookup = raw_input("What do you want to look up?")

searches = []
searches.append('corn')

ndbnos = []

for x in searches:
    userSearch = """https://api.nal.usda.gov/ndb/search/?format=json&q=""" + x + """&sort=n&max=1&offset=0&api_key=44wUlj8bxukI8IHQcFBNEBvi0G6yeafHaKWEdC7o"""
    response = requests.get(userSearch)
    json_data = json.loads(response.text)
    ndbnos.append(json_data['list']['item'][0]['ndbno'])

for y in ndbnos:
    print(y)
    userNutrients = """https://api.nal.usda.gov/ndb/reports/?ndbno=""" + y + """&type=b&format=json&api_key=44wUlj8bxukI8IHQcFBNEBvi0G6yeafHaKWEdC7o"""
    response2 = requests.get(userNutrients)
    json_data2 = json.loads(response2.text)
    print(json_data2['report']['food']['nutrients'][0]['value'])
    #['food']['nutrients'][0]['value']
#response = requests.get(userSearch)

#print(response.status_code)
#print(response.content)
