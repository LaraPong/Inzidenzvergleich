from flask import Flask, render_template, request

import sys
import time
from backend.suchfunktion import city_search
sys.path.append('/C/Users/abeer/PycharmProjects/pythonProject1/Inzidenzvergleich/vergleichNeu/backend')

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def home_page():

    formData = request.values
    spacing = "<br ><br>"
    # suchwort = "Ihre Suche" + spacing
    # suchwort2 = spacing
    if request.method == 'POST':
        # hier suche nach eienr wort
        suchwort = str(formData.get('input1'))
        suchwort2 = str(formData.get('input2'))
        #start = time.time()
        results = city_search(suchwort, suchwort2)
        #ende =  time.time()
        #seconds =ende-start
        return render_template('home.html', len=len(results), results=results ,suchwort=suchwort,suchwort2=suchwort2 )
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
