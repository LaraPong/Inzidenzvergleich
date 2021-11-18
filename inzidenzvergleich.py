from flask import Flask, render_template

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

@app.route("/")
def index():
    return render_template('abeer.html', action_url='localhost:3000/show')

@app.route("show")
def show():
    city_1 = requests.form.get('city_1')
    city_2 = requests.form.get('city_2')

    if(city_1 == 'Berlin'):
        incidence_1 = get_incidence(11)
    elif(city_1 == 'München'):
        incidence_1 = get_incidence(9162)
    elif(city_1 == 'Hamburg'):
        incidence_1 = get_incidence(2000)
    elif(city_1 == 'Köln')
        incidence_1 = get_incidence(5315)
    frankfurt = get_incidence(6412)
    stuttgart = get_incidence(8111)
    duesseldorf = get_incidence(5111)
    dortmund = get_incidence(5913)
    essen = get_incidence(5113)
    return render_template('show.html', berlin = berlin, hamburg = hamburg, cologne = cologne)