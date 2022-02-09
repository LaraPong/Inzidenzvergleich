from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime, timedelta

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




#def tableGetDate():
    #ToDo: Implement Database Call

    #return "1.1.2011"

@app.route("/", methods=['GET', 'POST'])
def homepage():

    suchdic1 = ["Dortmund", "Essen", "Berlin","München","Hamburg","Köln","Frankfurt","Stuttgart","Düsseldorf","Bremen","Dresden","Erfurt","Hannover","Kiel","Magdeburg","Mainz","Potsdam","Saarbrücken","Schwerin","Wiesbaden"
                "Manschester","Leeds", "Glasgow","Sheffield" , "Nottingham","NewcastleUponTyne", "Portsmouth","London", "Cardiff", "Belfast", "Liverpool" , "Birmingham" , "Edinburgh"]

    if request.method == 'POST':
        suchwort = request.form['input1']
        suchwort2 = request.form['input2']
        cursor = mysql.connection.cursor()

        select_incidence= f"SELECT * FROM inzidenzen_deutschland_{suchwort}"
        cursor.execute(select_incidence)
        results = cursor.fetchall()


        inzlist1=[row[2] for row in results]

        neulist=[]
        for row in results:
            neulist.append(str(row[1]))

        cursor = mysql.connection.cursor()
        select_incidence = f"SELECT * FROM inzidenzen_deutschland_{suchwort2}"
        cursor.execute(select_incidence)
        results2 = cursor.fetchall()

        inzlist2=[row[2] for row in results2]

        xwerte = [suchwort, suchwort2]

        y1 = inzlist1[len(inzlist1)-1]
        y2 = inzlist2[len(inzlist2)-1]

        ywerte = [y1, y2]



        error1 = None
        error2 = None

        if suchwort not in suchdic1:
            error1 = 'Stadt 1 nicht gültig'

        if suchwort2 not in suchdic1:
            error2 = 'Stadt 2 nicht gültig'

        if error1 or error2:
            return render_template('homepage.html', error1=error1, error2=error2, suchwort=suchwort, suchwort2=suchwort2)

        return render_template('homepage.html', suchwort=suchwort, suchwort2=suchwort2,ywerte=ywerte,xwerte=xwerte,
                                 inzlist2=inzlist2, inzlist1=inzlist1,neulist=neulist,suchdic1=suchdic1)

    else:

        return render_template('inzidenzdata.html',suchdic1=suchdic1)

@app.cli.command()    
def refresh_tables():
    """Refresh the tables from APIs"""
    city_dict = getBigCities()
    cur = mysql.connection.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    delete_date = (datetime.today() - timedelta(7)).strftime('%Y-%m-%d')
    for key, value in city_dict.items():
        table_city = key.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue") #aus Städtenamen Tabellennamen machen
        query = f"INSERT INTO inzidenzen_deutschland_{table_city} (datum, inzidenz) VALUES (%s, %s)"
        cur.execute(query, ({today}, {str(value)}))
        query_delete = f"DELETE FROM inzidenzen_deutschland_{table_city} WHERE datum < %s"
        cur.execute(query_delete, ({delete_date}))
        mysql.connection.commit()

if __name__ == "__main__":
   app.run(debug=True)
