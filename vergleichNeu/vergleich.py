import json

import flask
from flask import Flask, render_template, request
import os

import sys


from backend.suchfunktion import city_search, getBigCities

sys.path.append('/C/Users/abeer/PycharmProjects/pythonProject1/Inzidenzvergleich/vergleichNeu/backend')

app = Flask(__name__)

picklefolder=os.path.join('static','pics')

@app.route("/", methods=['GET', 'POST'])
def home_page():
    dict1=getBigCities()
    suchdic1 = [v for v in dict1.keys()]
    if request.method == 'POST':
        suchwort = request.form['input1']
        suchwort2 = request.form['input2']
        results = city_search(suchwort, suchwort2)
        xwerte = [v for v in results.keys()]
        ywerte = [x for x in results.values()]

        error1 = None
        error2 = None

        if suchwort not in  suchdic1:
            error1 = 'Stadt 1 nicht gültig'

        if suchwort2 not in  suchdic1:
            error2 = 'Stadt 2 nicht gültig'

        if error1 or error2:
            return render_template('home.html',  error1 = error1, error2 = error2)

        return render_template('home.html', results=results, suchwort=suchwort, suchwort2=suchwort2,xwerte=xwerte, ywerte=ywerte)
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
