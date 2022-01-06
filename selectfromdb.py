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

@app.route('/', methods=['GET', 'POST'])
#def get_incidence7days():
#    select_inzidence7days = "SELECT * FROM inzidenzen_deutschland_essen"
#    incidence7days = cursor.execute(select_inzidence7days)
#    return incidence7days

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
            select_inzidence_berlin = "SELECT * FROM inzidenzen_deutschland_berlin WHERE datum=%s"
            cursor.execute(select_inzidence_berlin, (current_date,))
            results = cursor.fetchall()

        if suchwort=='Essen':
            select_inzidence_essen = "SELECT * FROM inzidenzen_deutschland_essen WHERE datum=%s"
            cursor.execute(select_inzidence_essen, (current_date,))
            results = cursor.fetchall()

        return render_template('homepage.html', results=results, suchwort=suchwort, suchwort2=suchwort2)
    else:
        return render_template('homepage.html')


app.run(host='localhost', port=5000)
