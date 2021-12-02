from flask import Flask, render_template, request

import requests, json

app = Flask(__name__)

def get_incidence(city_id):
    url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/rki_key_data_v/FeatureServer/0/query?"
    parameter = {
        'referer':'https://www.mywebapp.com',
        'user-agent':'python-requests/2.9.1',
        'where': f'AdmUnitId = {city_id}', # Welche landkreise sollen zurück gegeben werden
        'outFields': '*', # Rückgabe aller Felder
        'returnGeometry': False, # Keine Geometrien
        'f':'json', # Rückgabeformat, hier JSON
        'cacheHint': True # Zugriff über CDN anfragen
    }
    result = requests.get(url=url, params=parameter) #Anfrage absetzen
    resultjson = json.loads(result.text) # Das Ergebnis JSON als Python Dictionary laden
    incidence = resultjson['features'][0]['attributes']['Inz7T']
    return incidence

def getBigCities():
    cities_incidences = {}
    
    big_cities = {# Das irgendwann direkt aus Datenbank oder Tabelle ablesen
      'Berlin': 11,
      'München': 9162,
      'Hamburg': 2000,
      'Köln': 5315,
      'Frankfurt': 6412,
      'Stuttgart': 8111,
      'Düsseldorf': 5111,
      'Dortmund': 5913,
      'Essen': 5113 }
    
    for key, value in big_cities.items():
        cities_incidences[key] = get_incidence(value)
    return cities_incidences

city_dict = getBigCities()

def city_search(city1, city2):
    list = []

    for key, value in city_dict.items():
        if city1 in key:
            list.append(city1)
            list.append(value)

        if city2 in key:
            list.append(city2)
            list.append(value)

    return list

@app.route("/", methods=['GET', 'POST'])
def homepage():
    formData = request.values
    if (request.method == 'POST' and formData.get('freshData')):
        return render_template('homepage.html', results=results, suchwort=suchwort, suchwort2=suchwort2)
    else:
        return render_template('homepage.html')


if __name__ == "__main__":
    app.debug = True
    app.run()

 
