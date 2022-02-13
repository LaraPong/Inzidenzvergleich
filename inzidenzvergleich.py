from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime, timedelta
import requests, json
import folium

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
    suchdic1 = ["Dortmund", "Essen", "Berlin","Muenchen","Hamburg","Koeln","Frankfurt","Stuttgart","Duesseldorf","Bremen","Dresden","Erfurt","Hannover","Kiel","Magdeburg","Mainz","Potsdam","Saarbruecken","Schwerin","Wiesbaden"
                "Manchester","Leeds", "Glasgow","Sheffield" , "Nottingham","NewcastleUponTyne", "Portsmouth","London", "Cardiff", "Belfast", "Liverpool" , "Birmingham" , "Edinburgh"]

    if request.method == 'POST':

        suchwort = request.form['input1']
        #suchwort = key.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue")
        suchwort2 = request.form['input2']
       # suchwort2 = key.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue")
        cursor = mysql.connection.cursor()

        error1 = None
        error2 = None

        if suchwort not in suchdic1:
           error1 = 'Stadt 1 nicht gültig'

        if suchwort2 not in suchdic1:
           error2 = 'Stadt 2 nicht gültig'

        if error1 or error2:
            return render_template('homepage.html', error1=error1, error2=error2,suchdic1=suchdic1,suchwort2=suchwort2,suchwort=suchwort)


        select_incidence= f"SELECT * FROM inzidenzen_{suchwort}"
        cursor.execute(select_incidence)
        results = cursor.fetchall()


        inzlist1=[row[2] for row in results]

        neulist=[]
        for row in results:
            neulist.append(str(row[1]))

        cursor = mysql.connection.cursor()
        select_incidence = f"SELECT * FROM inzidenzen_{suchwort2}"
        cursor.execute(select_incidence)
        results2 = cursor.fetchall()

        inzlist2=[row[2] for row in results2]

        xwerte = [suchwort, suchwort2]

        y1 = inzlist1[len(inzlist1)-1]
        y2 = inzlist2[len(inzlist2)-1]

        ywerte = [y1, y2]


        return render_template('homepage.html', suchwort=suchwort, suchwort2=suchwort2, ywerte=ywerte, xwerte=xwerte,
                                 inzlist2=inzlist2, inzlist1=inzlist1,neulist=neulist,suchdic1=suchdic1)

    else:

        return render_template('homepage.html',suchdic1=suchdic1)

@app.route("/")
def index():

    cursor = mysql.connection.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    cursor=mysql.connection.cursor()

    select_inzidenzen = f"SELECT essen.datum, essen.inzidenz as essen WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    essen_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT wiesbaden.datum, wiesbaden.inzidenz as wiesbaden WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    wiesbaden_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT stuttgart.datum, stuttgart.inzidenz as stuttgart WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    stuttgart_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT schwerin.datum, schwerin.inzidenz as schwerin WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    schwerin_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT berlin.datum, berlin.inzidenz as berlin WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    berlin_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT saarbruecken.datum, saarbruecken.inzidenz as saarbruecken WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    saarbruecken_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT potsdam.datum, potsdam.inzidenz as potsdam WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    potsdam_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT muenchen.datum, muenchen.inzidenz as muenchen WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    muenchen_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT mainz.datum, mainz.inzidenz as mainz WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    mainz_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT koeln.datum, koeln.inzidenz as koeln WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    koeln_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT kiel.datum, kiel.inzidenz as kiel WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    kiel_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT dortmund.datum, dortmund.inzidenz as dortmund WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    dortmund_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT hannover.datum, hannover.inzidenz as hannover WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    hannover_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT hamburg.datum, hamburg.inzidenz as hamburg WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    hamburg_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT frankfurt.datum, frankfurt.inzidenz as frankfurt WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    frankfurt_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT dresden.datum, dresden.inzidenz as dresden WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    dresden_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT bremen.datum, bremen.inzidenz as bremen WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    bremen_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT belfast.datum, belfast.inzidenz as belfast WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    belfast_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT birmingham.datum, birmingham.inzidenz as birmingham WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    birmingham_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT cardiff.datum, cardiff.inzidenz as cardiff WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    cardiff_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT edinburgh.datum, edinburgh.inzidenz as edinburgh WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    edinburgh_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT glasgow.datum, glasgow.inzidenz as glasgow WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    glasgow_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT leeds.datum, leeds.inzidenz as leeds WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    leeds_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT liverpool.datum, liverpool.inzidenz as liverpool WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    liverpool_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT london.datum, london.inzidenz as london WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    london_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT manchester.datum, manchester.inzidenz as manchester WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    manchester_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT newcastleupontyne.datum, newcastleupontyne.inzidenz as newcastleupontyne WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    newcastleupontyne_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT nottingham.datum, nottingham.inzidenz as nottingham WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    nottingham_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT portsmouth.datum, portsmouth.inzidenz as portsmouth WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    portsmouth_inz=cursor.fetchall()

    select_inzidenzen = f"SELECT sheffield.datum, sheffield.inzidenz as sheffield WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    sheffield_inz=cursor.fetchall()


    select_inzidenzen = f"SELECT duesseldorf.datum, duesseldorf.inzidenz as duesseldorf WHERE datum=%s LIMIT 1"
    cursor.execute(select_inzidenzen, ({today}))
    cursor.commit()
    duesseldorf_inz=cursor.fetchall()


    map = folium.Map(location=[51,3], zoom_start=2)
    folium.Marker(location=[52.523430,13.411440], popups="Berlin", tooltip={'Berlin', berlin_inz}).add_to(map)
    folium.Marker(location=[48.1371079,11.5753822], popups="muenchen", tooltip={'München', muenchen_inz}).add_to(map)
    folium.Marker(location=[53.550341,10.000654], popups="Hamburg", tooltip={'Hamburg', hamburg_inz}).add_to(map)
    folium.Marker(location=[50.938361,6.959974], popups="Köln", tooltip={'Köln', koeln_inz}).add_to(map)
    folium.Marker(location=[50.1106444,8.6820917], popups="Frankfurt", tooltip={'Frankfurt', frankfurt_inz}).add_to(map)
    folium.Marker(location=[48.7784485,9.1800132], popups="Stuttgart", tooltip={'Stuttgart', stuttgart_inz}).add_to(map)
    folium.Marker(location=[51.2254018,6.7763137], popups="Düsseldorf", tooltip={'Düsseldorf', duesseldorf_inz}).add_to(map)
    folium.Marker(location=[51.5142273,7.4652789], popups="Dortmund", tooltip={'Dortmund',dortmund_inz }).add_to(map)
    folium.Marker(location=[51.4582235,7.0158171], popups="Essen", tooltip={'Essen', essen_inz}).add_to(map)
    folium.Marker(location=[53.6288297,11.4148038], popups="Schwerin", tooltip={'Schwerin', schwerin_inz}).add_to(map)
    folium.Marker(location=[54.3227085,10.135555], popups="Kiel", tooltip={'Kiel', kiel_inz}).add_to(map)
    folium.Marker(location=[49.234362,6.996379], popups="Saarbrücken", tooltip={'Saarbrücken', saarbruecken_inz}).add_to(map)
    folium.Marker(location=[50.0820384,8.2416556], popups="Wiesbaden", tooltip={'Wiesbaden', wiesbaden_inz}).add_to(map)
    folium.Marker(location=[52.4009309,13.0591397], popups="Potsdam", tooltip={'Potsdam', potsdam_inz}).add_to(map)
    folium.Marker(location=[50.0012314,50.0012314], popups="Mainz", tooltip={'Mainz', mainz_inz}).add_to(map)
    folium.Marker(location=[51.0493286,13.7381437], popups="Dresden", tooltip={'Dresden', dresden_inz}).add_to(map)
    folium.Marker(location=[53.0758196,8.8071646], popups="Bremen", tooltip={'Bremen', bremen_inz}).add_to(map)
    folium.Marker(location=[52.3744779,9.7385532], popups="Hannover", tooltip={'Hannover',hannover_inz}).add_to(map)

   #Magdeburg
   #Erfurt

    folium.Marker(location=[53.480709, -2.234380], popups="Manchester", tooltip={'Manchester', manchester_inz}).add_to(map)
    folium.Marker(location=[53.799690, -1.549100], popups="Leeds", tooltip={'Leeds', leeds_inz}).add_to(map)
    folium.Marker(location=[55.865681, -4.257140], popups="Glasgow", tooltip={'Glasgow', glasgow_inz}).add_to(map)
    folium.Marker(location=[53.383060, -1.464800], popups="Sheffield", tooltip={'Sheffield', sheffield_inz}).add_to(map)
    folium.Marker(location=[52.9534193, -1.1496461], popups="Nottingham", tooltip={'Nottingham',nottingham_inz}).add_to(map)
    folium.Marker(location=[51.4816546, -3.1791934], popups="Cardiff", tooltip={'Cardiff', cardiff_inz}).add_to(map)
    folium.Marker(location=[54.596391, -5.9301829], popups="Belfast", tooltip={'Belfast', belfast_inz}).add_to(map)
    folium.Marker(location=[53.4071991, -2.99168], popups="Liverpool", tooltip={'Liverpool', liverpool_inz}).add_to(map)
    folium.Marker(location=[52.4796992, -1.9026911], popups="Birmingham", tooltip={'Birmingham', birmingham_inz }).add_to(map)
    folium.Marker(location=[55.9533456, -3.1883749], popups="Edinburgh", tooltip={'Edinburgh', edinburgh_inz}).add_to(map)
    folium.Marker(location=[51.5073219, -0.1276474], popups="London", tooltip={'London', london_inz}).add_to(map)
    folium.Marker(location=[50.8036831, -1.075614], popups="Portsmouth", tooltip={'Portsmouth', portsmouth_inz}).add_to(map)
    folium.Marker(location=[55.116825103759766, -1.9396450519561768], popups="NewcastleUponTyne", tooltip={'Newcastle Upon Tyne', newcastleupontyne_inz}).add_to(map)




    map.save('templates/map.html')
    return render_template('homepage.html')


@app.route('/map')
def map():
    return render_template('map.html')

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
