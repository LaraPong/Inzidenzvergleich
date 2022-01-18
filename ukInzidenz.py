from flask import Flask, render_template, request

import requests, json
from requests import get
from json import dumps

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

    # get_incidence Großbritanien


def get_incidence_uk(city_id):
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

        "dailyCases": "newCasesByPublishDate",
    }

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":")),
        "latestBy": "cumCasesByPublishDate"
    }

    api_params["format"] = "json"
    response = get(ENDPOINT, params=api_params, timeout=10)
    assert response.status_code == 200, f"Failed request for {fmt}: {response.text}"
    json_content = response.json()
    return json_content["data"][0]["dailyCases"]


# Funktion ruft Inzidenzen für 10 gr Städte auf und speichert sie in dictionary

def getBigCities():
    cities_incidences = {}

    manchester = get_incidence_uk("E08000003")
    leeds = get_incidence_uk("E08000035")
    glasgow = get_incidence_uk("S12000049")
    sheffield = get_incidence_uk("E08000019")
    nottingham = get_incidence_uk("E06000018")
    newcastleUponTyne = get_incidence_uk("E08000021")
    portsmouth = get_incidence_uk("E06000044")
    cardiff = get_incidence_uk("W06000015")
    belfast = get_incidence_uk("N09000003")
    liverpool = get_incidence_uk("E08000012")
    birmingham = get_incidence_uk("E08000025")
    edinburgh = get_incidence_uk("S12000036")
    london = get_incidence_uk("E12000007")
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