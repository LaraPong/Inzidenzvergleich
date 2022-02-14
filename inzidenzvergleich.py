import requests, json
import folium
from flask import Flask, render_template, request
from requests import get
from flask_mysqldb import MySQL
from datetime import datetime, timedelta
from json import dumps

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



def get_incidence_br(city_id):
    
    if city_id == "E12000007":
        AREA_TYPE = "region"
    else:
        AREA_TYPE = "ltla"
        
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    AREA_CODE = city_id;

    filters = [
         f"areaType={AREA_TYPE}",
         f"areaCode={AREA_CODE}"

    ]

    structure = {

        "dailyCases" : "newCasesByPublishDate",
    }

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":")),
     "latestBy": "cumCasesByPublishDate"
    }

    api_params["format"] = "json"
    response = get(ENDPOINT, params=api_params, timeout=10)
    assert response.status_code == 200, f"Failed request for json: {response.text}"
    json_content = response.json()
    print(" ")
    print(json_content["data"][0]["dailyCases"]) 


def get_big_cities():
    dict={}
    dict['Berlin'] = get_incidence(11)
    dict['München'] = get_incidence(9162)
    dict['Hamburg'] = get_incidence(2000)
    dict['Köln'] = get_incidence(5315)
    dict['Frankfurt'] = get_incidence(6412)
    dict['Stuttgart'] = get_incidence(8111)
    dict['Düsseldorf'] = get_incidence(5111)
    dict['Dortmund'] = get_incidence(5913)
    dict['Essen'] = get_incidence(5113)

    dict['Manchester'] = get_incidence_br("E08000003")
    dict['Leeds'] = get_incidence_br("E08000035")
    #dict['Glasgow'] = get_incidence_br("S12000049")
    dict['Sheffield'] = get_incidence_br("E08000019")
    dict['Nottingham'] = get_incidence_br("E06000018")
    dict['NewcastleUponTyne'] = get_incidence_br("E08000021")
    dict['Portsmouth'] = get_incidence_br("E06000044")
    dict['London'] = get_incidence_br("E12000007")
    dict['Cardiff'] = get_incidence_br("W06000015")
    dict['Belfast'] = get_incidence_br("N09000003")
    dict['Liverpool'] = get_incidence_br("E08000012")
    dict['Birmingham'] = get_incidence_br("E08000025")
    #dict['Edinburgh'] = get_incidence_br("S12000036")
    

    return dict

@app.route("/", methods=['GET', 'POST'])
def homepage():
    suchdic1 = ["dortmund", "essen", "berlin","muenchen","hamburg","koeln","frankfurt","stuttgart","duesseldorf","bremen","dresden","erfurt","hannover","kiel","magdeburg","mainz","potsdam","saarbrücken","schwerin","wiesbaden"
                "manchester","leeds", "glasgow","sheffield" , "nottingham","newcastleUponTyne", "portsmouth","london", "cardiff", "belfast", "liverpool" , "birmingham" , "edinburgh"]


    if request.method == 'POST':
        suchwort = request.form['input1']
        #suchwort = key.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue")
        suchwort2 = request.form['input2']
       # suchwort2 = key.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue")
        cursor = mysql.connection.cursor()

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


    map = folium.Map(location=[51,3], zoom_start=5)
    folium.Marker(location=[52.523430,13.411440], popups="Berlin", tooltip={'Berlin', berlin_inz}).add_to(map)
    folium.Marker(location=[48.1371079,11.5753822], popups="München", tooltip={'München', muenchen_inz}).add_to(map)
    folium.Marker(location=[53.550341,10.000654], popups="Hamburg", tooltip={'Hamburg', hamburg_inz}).add_to(map)
    folium.Marker(location=[50.938361,6.959974], popups="Köln", tooltip={'Köln', koeln_inz}).add_to(map)
    folium.Marker(location=[50.1106444,8.6820917], popups="Frankfurt", tooltip={'Frankfurt', frankfurt_inz}).add_to(map)
    folium.Marker(location=[48.7784485,9.1800132], popups="Stuttgart", tooltip={'Stuttgart', stuttgart_inz}).add_to(map)
    folium.Marker(location=[51.2254018,6.7763137], popups="Düsseldorf", tooltip={'Düsseldorf', duesseldorf_inz}).add_to(map)
    folium.Marker(location=[51.5142273,7.4652789], popups="Dortmund", tooltip={'Dortmund',dortmund_inz }).add_to(map)
    folium.Marker(location=[51.4582235,7.0158171], popups="Essen", tooltip={'Essen', essen_inz}).add_to(map)

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


    map.save('templates/map.html')
    return render_template('homepage.html',y3=y3)


@app.route('/map')
def map():
    return render_template('map.html')
    
@app.cli.command()    
def refresh_tables():
    """Refresh the tables from APIs"""
    city_dict = get_big_cities()
    cur = mysql.connection.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    delete_date = (datetime.today() - timedelta(7)).strftime('%Y-%m-%d')
    for key, value in city_dict.items():
        table_city = key.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue") #aus Städtenamen Tabellennamen machen
        query = f"INSERT INTO inzidenzen_{table_city} (datum, inzidenz) VALUES (%s, %s)"
        cur.execute(query, ({today}, {str(value)}))
        query_delete = f"DELETE FROM inzidenzen_{table_city} WHERE datum < %s"
        cur.execute(query_delete, ({delete_date}))
        mysql.connection.commit()

if __name__ == "__main__":
   app.run(debug=True)
