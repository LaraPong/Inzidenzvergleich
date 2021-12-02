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
    berlin = get_incidence(11)
    munich = get_incidence(9162)
    hamburg= get_incidence(2000)
    cologne = get_incidence(5315)
    frankfurt = get_incidence(6412)
    stuttgart = get_incidence(8111)
    duesseldorf = get_incidence(5111)
    dortmund = get_incidence(5913)
    essen = get_incidence(5113)

    dict={}
    dict['Berlin'] =berlin
    dict['München'] = munich
    dict['Hamburg'] = hamburg
    dict['Köln'] = cologne
    dict['Frankfurt'] = frankfurt
    dict['Stuttgart'] = stuttgart
    dict['Düsseldorf'] = duesseldorf
    dict['Dortmund'] = dortmund
    dict['Essen'] = essen

    return dict

city_dict = getBigCities()

def city_search(city1, city2):
    info = {}

    for key, value in city_dict.items():
        if city1 in key:
            info.update({city1: value})

        if city2 in key:
            info.update({city2: value})
    return (info)


@app.route("/", methods=['GET', 'POST'])
def homepage():
    formData = request.values
    spacing = "<br ><br>"
    if request.method == 'POST':

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
