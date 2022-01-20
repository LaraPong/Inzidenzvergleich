from flask import Flask, render_template, request

import requests, json
from requests import get
from json import dumps
import datetime as DT

app = Flask(__name__)


def get_incidence(city_id):
    url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/rki_key_data_v/FeatureServer/0/query?"
    parameter = {
        'referer': 'https://www.mywebapp.com',
        'user-agent': 'python-requests/2.9.1',
        'where': f'AdmUnitId = {city_id}',  # Welche landkreise sollen zurück gegeben werden
        'outFields': '*',  # Rückgabe aller Felder
        'returnGeometry': False,  # Keine Geometrien
        'f': 'json',  # Rückgabeformat, hier JSON
        'cacheHint': True  # Zugriff über CDN anfragen
    }
    result = requests.get(url=url, params=parameter)  # Anfrage absetzen
    resultjson = json.loads(result.text)  # Das Ergebnis JSON als Python Dictionary laden
    incidence = resultjson['features'][0]['attributes']['Inz7T']
    return incidence

    # get_dailyCases Großbritanien

def get_dailyCases_uk (city_id, date):
    
    if city_id == "E12000007":
        AREA_TYPE = "region"
    else:
        AREA_TYPE = "ltla"
        
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    AREA_CODE = city_id;
    DATE = date

    filters = [
         f"areaType={AREA_TYPE}",
         f"areaCode={AREA_CODE}",
         f"date={DATE}"

    ]

    structure = {

        "dailyCases" : "newCasesByPublishDate",
    }

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":")),
     
    }

    api_params["format"] = "json"
    response = get(ENDPOINT, params=api_params, timeout=10)
    assert response.status_code == 200, f"Failed request for {fmt}: {response.text}"
    json_content = response.json()
    return json_content["data"][0]["dailyCases"]
    
    # get_incidence_uk hier wird die 7-Tage Inzidenz für UK aus den DailyCases berechnet 

def get_incidence_uk (city_id, population):
    today = DT.date.today()
    date1 = today - DT.timedelta(days=1)
    date2 = today - DT.timedelta(days=2)
    date3 = today - DT.timedelta(days=3)
    date4 = today - DT.timedelta(days=4)
    date5 = today - DT.timedelta(days=5)
    date6 = today - DT.timedelta(days=6)
    date7 = today - DT.timedelta(days=7)

    day1 = get_dailyCases_uk(city_id, date1)
    day2 = get_dailyCases_uk(city_id, date2)
    day3 = get_dailyCases_uk(city_id, date3)
    day4 = get_dailyCases_uk(city_id, date4)
    day5 = get_dailyCases_uk(city_id, date5)
    day6 = get_dailyCases_uk(city_id, date6)
    day7 = get_dailyCases_uk(city_id, date7)
    
    dailyCasesSum = day1 + day2 + day3 + day4 + day5 + day6 + day7
    incidence = (dailyCasesSum / population) * 100000

    return round(incidence, 1)


# Funktion ruft Inzidenzen für 10 gr Städte auf und speichert sie in dictionary

def getBigCities():
    cities_incidences = {}

    manchester = get_incidence_uk("E08000003", 553230)
    leeds = get_incidence_uk("E08000035", 792525)
    glasgow =get_incidence_uk("S12000049", 1861315)
    sheffield = get_incidence_uk("E08000019", 1569000)
    nottingham = get_incidence_uk("E06000018", 331297)
    newcastleUponTyne = get_incidence_uk("E08000021", 302820)
    portsmouth = get_incidence_uk("E06000044", 1547000)
    cardiff = get_incidence_uk("W06000015", 1097000)
    belfast = get_incidence_uk("N09000003", 343000)
    liverpool = get_incidence_uk("E08000012", 496784)
    birmingham = get_incidence_uk("E08000025", 1149000)
    edinburgh = get_incidence_uk("S12000036", 525000)
    london = get_incidence_uk("E12000007", 8982000)
    berlin = get_incidence(11)
    munich = get_incidence(9162)
    hamburg = get_incidence(2000)
    cologne = get_incidence(5315)
    frankfurt = get_incidence(6412)
    stuttgart = get_incidence(8111)
    duesseldorf = get_incidence(5111)
    dortmund = get_incidence(5913)
    essen = get_incidence(5113)

    dict = {}
    dict['Manschester'] = manchester
    dict['Leeds'] = leeds
    dict['Glasgow'] = glasgow
    dict['Sheffield'] = sheffield
    dict['Nottingham'] = nottingham
    dict['NewcastleUponTyne'] = newcastleUponTyne
    dict['Portsmouth'] = portsmouth
    dict['Cardiff'] = cardiff
    dict['Belfast'] = belfast
    dict['Liverpool'] = liverpool
    dict['Birmingham'] = birmingham
    dict['Edinburgh'] = edinburgh
    dict['London'] = london
    dict['Berlin'] = berlin
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


def tableGetDate():
    # ToDo: Implement Database Call

    return "1.1.2011"


@app.route("/", methods=['GET', 'POST'])
def homepage():
    dict1 = getBigCities()
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
            return render_template('homepage.html', error1=error1, error2=error2, suchwort=suchwort,
                                   suchwort2=suchwort2)

        return render_template('homepage.html', results=results, suchwort=suchwort, suchwort2=suchwort2, xwerte=xwerte,
                               ywerte=ywerte)
    else:
        return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)