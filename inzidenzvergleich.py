from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import requests, json


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inzidenzen'
app.config['MYSQL_SQL_MODE'] = 'NO_AUTO_VALUE_ON_ZERO'
mysql = MySQL(app)
today = ''

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


#def tableGetDate():
    #ToDo: Implement Database Call
    
    #return "1.1.2011"

@app.route("/", methods=['GET', 'POST'])
def homepage():
   # dict1 = getBigCities()
    #suchdic1 = [v for v in dict1.keys()]
    if request.method == 'POST':
        suchwort = request.form['input1']
        suchwort2 = request.form['input2']
        cursor = mysql.connection.cursor()
        select_incidence= f"SELECT * FROM inzidenzen_deutschland_{suchwort}"
        cursor.execute(select_incidence)
        results = cursor.fetchall()

        print(results)
        select_date = f"SELECT datum FROM inzidenzen_deutschland_{suchwort}"
        cursor.execute(select_date)
        resultdate = cursor.fetchall()

        inzlist1=[row[2] for row in results]

        neulist=[]
        for row in results:
            neulist.append(str(row[1]))


        cursor = mysql.connection.cursor()
        select_incidence = f"SELECT * FROM inzidenzen_deutschland_{suchwort2}"
        cursor.execute(select_incidence)
        results2 = cursor.fetchall()

        inzlist2=[row[2] for row in results2]

        #results = city_search(suchwort, suchwort2)
        #xwerte = [v for v in results.keys()]
        # ywerte = [x for x in results.values()]
        # y1 , y2 inzidenzwert für je suchwort
        #y1= results[suchwort]
        # y2= results[suchwort2]
        # st1, st2 beispiel für 7 Tag von inzidenzwert
         # dat beispiel für datum
        #dat=resultdate


        #error1 = None
       # error2 = None

       # if suchwort not in suchdic1:
           # error1 = 'Stadt 1 nicht gültig'

       # if suchwort2 not in suchdic1:
           # error2 = 'Stadt 2 nicht gültig'

      #  if error1 or error2:
           # return render_template('homepage.html', error1=error1, error2=error2, suchwort=suchwort, suchwort2=suchwort2)

        return render_template('homepage.html', suchwort=suchwort, suchwort2=suchwort2,
                                 inzlist2=inzlist2, inzlist1=inzlist1,neulist=neulist)
    else:
        return render_template('homepage.html')

if __name__ == "__main__":
   app.run(debug=True)
