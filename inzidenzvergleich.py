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


# Funktion ruft Inzidenzen für 10 gr Städte auf und speichert sie in dictionary

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
    info = {}

    for key, value in city_dict.items():
        if city1 in key:
            info.update({city1: value})

        if city2 in key:
            info.update({city2: value})
    return (info)


def tableGetDate():
    #ToDo: Implement Database Call
    
    return "1.1.2011"

@app.route("/", methods=['GET', 'POST'])
def homepage():
    formData = request.values
    if (request.method == 'POST' and formData.get('freshData')):

        return render_template('homepage.html', date = tableGetDate()) #ToDo: Persist data from respective other if condition, with hidden fields? Multi-page-app?
    elif (request.method == 'POST' and formData.get('freshData')):
        suchwort = str(formData.get('input1'))
        suchwort2 = str(formData.get('input2'))
        results = city_search(suchwort, suchwort2)

        #labels = [suchwort, suchwort2]
        
        xwerte = [v for v in results.keys()]
        ywerte = [x for x in results.values()]


        return render_template('homepage.html', results=results, suchwort=suchwort, suchwort2=suchwort2, xwerte=xwerte, ywerte=ywerte)
    else:
        return render_template('homepage.html')


if __name__ == "__main__":
   app.run(debug=True)
