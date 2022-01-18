from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime, timedelta

import requests, json, time, atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inzidenzen'
app.config['MYSQL_SQL_MODE'] = 'NO_AUTO_VALUE_ON_ZERO'
mysql = MySQL(app)

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

@app.before_first_request
def refresh_tables():
    city_dict = getBigCities()
    cur = mysql.connection.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    delete_date = (datetime.today() - timedelta(7)).strftime('%Y-%m-%d')
    print("I'm running")
    for key, value in city_dict.items():
        table_city = key.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue") #aus Städtenamen Tabellennamen machen
        query = f"INSERT INTO inzidenzen_deutschland_{table_city} (datum, inzidenz) VALUES ({today}, {value})"
        cur.execute(query)
        mysql.connection.commit()
        query_delete = f"DELETE FROM inzidenzen_deutschland_{table_city} WHERE datum < {delete_date}"
        cur.execute(query_delete) #todo: Return last refreshed and post to website

#scheduler = BackgroundScheduler()
#scheduler.add_job(func=refresh_tables, trigger="interval", seconds=60)
#scheduler.start()

#atexit.register(lambda: scheduler.shutdown())
    

@app.route("/", methods=['GET', 'POST'])
def homepage():
    formData = request.values

    if request.method == 'POST':
        suchwort = str(formData.get('input1'))
        suchwort2 = str(formData.get('input2'))
        cursor = mysql.connection.cursor()
        if suchwort=='Berlin':
            select_inzidence_berlin = "SELECT inzidenz FROM inzidenzen_deutschland_berlin "
            cursor.execute(select_inzidence_berlin)
            results = cursor.fetchall()

        if suchwort2 == 'Berlin':
            select_inzidence_berlin = "SELECT inzidenz FROM inzidenzen_deutschland_berlin "
            cursor.execute(select_inzidence_berlin)
            results2 = cursor.fetchall()

        if suchwort=='Essen':
            select_inzidence_essen = "SELECT datum, inzidenz FROM inzidenzen_deutschland_essen"
            cursor.execute(select_inzidence_essen)
            results = cursor.fetchall()

        if suchwort2 == 'Essen':
            select_inzidence_essen = "SELECT datum, inzidenz FROM inzidenzen_deutschland_essen"
            cursor.execute(select_inzidence_essen)
            results2 = cursor.fetchall()

        if suchwort == 'Bremen':
            select_inzidence_bremen = "SELECT datum, inzidenz FROM inzidenzen_deutschland_bremen"
            cursor.execute(select_inzidence_bremen)
            results = cursor.fetchall()

        if suchwort2 == 'Bremen':
            select_inzidence_bremen = "SELECT datum, inzidenz FROM inzidenzen_deutschland_bremen"
            cursor.execute(select_inzidence_bremen)
            results2 = cursor.fetchall()

        if suchwort=='Dortmund':
            select_inzidence_dortmund = "SELECT datum, inzidenz FROM inzidenzen_deutschland_dortmund"
            cursor.execute(select_inzidence_dortmund)
            results = cursor.fetchall()

        if suchwort2 == 'Dortmund':
            select_inzidence_dortmund = "SELECT datum, inzidenz FROM inzidenzen_deutschland_dortmund"
            cursor.execute(select_inzidence_dortmund)
            results2 = cursor.fetchall()

        if suchwort=='Dresden':
            select_inzidence_dresden = "SELECT datum, inzidenz FROM inzidenzen_deutschland_dresden"
            cursor.execute(select_inzidence_dresden)
            results = cursor.fetchall()

        if suchwort2 == 'Dresden':
            select_inzidence_dresden = "SELECT datum, inzidenz FROM inzidenzen_deutschland_dresden"
            cursor.execute(select_inzidence_dresden)
            results2 = cursor.fetchall()

        if suchwort=='Düsseldorf':
            select_inzidence_duesseldorf = "SELECT datum, inzidenz FROM inzidenzen_deutschland_duesseldorf"
            cursor.execute(select_inzidence_duesseldorf)
            results = cursor.fetchall()

        if suchwort=='Erfurt':
            select_inzidence_erfurt = "SELECT datum, inzidenz FROM inzidenzen_deutschland_erfurt"
            cursor.execute(select_inzidence_erfurt)
            results = cursor.fetchall()

        if suchwort=='Frankfurt':
            select_inzidence_frankfurt = "SELECT datum, inzidenz FROM inzidenzen_deutschland_frankfurt"
            cursor.execute(select_inzidence_frankfurt)
            results = cursor.fetchall()

        if suchwort=='Hamburg':
            select_inzidence_hamburg = "SELECT datum, nzidenz FROM inzidenzen_deutschland_hamburg"
            cursor.execute(select_inzidence_hamburg)
            results = cursor.fetchall()

        if suchwort=='Hannover':
            select_inzidence_hannover = "SELECT datum, inzidenz FROM inzidenzen_deutschland_hannover"
            cursor.execute(select_inzidence_hannover)
            results = cursor.fetchall()

        select_berlin = "SELECT datum, inzidenz FROM inzidenzen_deutschland_berlin"
        berlin = cursor.execute(select_berlin)
        select_essen = "SELECT datum, inzidenz FROM inzidenzen_deutschland_essen"
        essen = cursor.execute(select_essen)

        dict = {}
        dict['Berlin'] = berlin
        dict['Essen'] = essen

        return render_template('inzidenzdata.html', results=results, results2=results2, suchwort=suchwort, suchwort2=suchwort2)
    else:
        return render_template('inzidenzdata.html')

if __name__ == "__main__":
   app.run(debug=True)
