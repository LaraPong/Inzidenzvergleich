from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inzidenzen'
app.config['MYSQL_SQL_MODE'] = 'NO_AUTO_VALUE_ON_ZERO'
#Entsprechend anpassen, wenn auf Server:
#IP-Adresse: siehe Slack
#User: siehe Slack
#Password User Root: siehe Slack

mysql = MySQL(app)

#cursor = mysql.connection.cursor()

@app.route('/', methods=['GET', 'POST'])
#def get_incidence7days():
    #formData = request.values
    #spacing = "<br ><br>"
    #cursor = mysql.connection.cursor()
    #if request.method == 'POST':
    #    select_inzidence7days = "SELECT * FROM inzidenzen_deutschland_essen"
    #    incidence7days = cursor.execute(select_inzidence7days)
    #return incidence7days

#def getBigCities():
#    select_berlin = "SELECT * FROM inzidenzen_deutschland_berlin WHERE datum=%s"
#    berlin = cursor.execute(select_berlin, (current_date,))
#    select_essen = "SELECT * FROM inzidenzen_deutschland_essen WHERE datum=%s"
#    essen = cursor.execute(select_essen, (current_date,))

#    dict={}
#    dict['Berlin'] =berlin
#    dict['Essen'] = essen

#    return dict

#city_dict = getBigCities()

#def city_search(city1, city2):
#    list = []

#    for key, value in city_dict.items():
#        if city1 in key:
#            list.append(city1)
#            list.append(value)

#        if city2 in key:
 #           list.append(city2)
 #           list.append(value)

#    return list



def homepage():
    formData = request.values
    spacing = "<br ><br>"
    now = datetime.now()
    current_date = now.strftime('%Y-%m-%d')
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

        return render_template('map.html', results=results, results2=results2, suchwort=suchwort, suchwort2=suchwort2)
    else:
        return render_template('map.html')


app.run(host='localhost', port=5000)
