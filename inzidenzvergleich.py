from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime

import requests, json, time

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inzidenzen'
app.config['MYSQL_SQL_MODE'] = 'NO_AUTO_VALUE_ON_ZERO'

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

#@app.before_first_request
def refresh_tables(city_dict):
    mysql = MySQL(app)
    cur = mysql.connection.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    id_counter = 2
    while True:
        for key, value in city_dict.items():
            table_city = key.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue") #aus Städtenamen Tabellennamen machen
            query = f"INSERT INTO inzidenzen.inzidenzen_deutschland_{table_city} (id, datum, inzidenz) VALUES ({id_counter}, {today}, {value})"
            cur.execute(query)
            id_counter += 1
            print(id_counter)
        time.sleep(3600*24) #einen Tag warten, bevor die Schleife wieder ausgeführt wird; funktioniert nicht! Mit "sched" probieren/threading!
    #todo: zuletzt aktualisiert in frontend ausgeben

@app.route("/", methods=['GET', 'POST'])
def homepage():
    dict1 = getBigCities()
    refresh_tables(dict1)
    suchdic1 = [v for v in dict1.keys()]
    if request.method == 'POST':
        suchwort = request.form['input1']
        suchwort2 = request.form['input2']
        results = city_search(suchwort, suchwort2)
        xwerte = [v for v in results.keys()]
        ywerte = [x for x in results.values()]

        error1 = None
        error2 = None

        if suchwort not in suchdic1:
            error1 = 'Stadt 1 nicht gültig'

        if suchwort2 not in suchdic1:
            error2 = 'Stadt 2 nicht gültig'

        if error1 or error2:
            return render_template('homepage.html', error1=error1, error2=error2, suchwort=suchwort, suchwort2=suchwort2)

        return render_template('homepage.html', results=results, suchwort=suchwort, suchwort2=suchwort2, xwerte=xwerte,
                               ywerte=ywerte)
    else:
        return render_template('homepage.html')

if __name__ == "__main__":
   app.run(debug=True)
