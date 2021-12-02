import matplotlib
import requests, json
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
import pyqtgraph as pg
import os




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


diccity=city_search("Dortmund", "Essen")

