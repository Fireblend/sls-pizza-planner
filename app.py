import json
from datetime import datetime, timedelta
from flask import Flask, request, render_template
from pizza import get_pizza_data

app = Flask(__name__)

def readLang(file):
    with open(f'langs/{file}.json') as f:
        return json.load(f)

lang_files = ["en", "es"]
langs = {x:readLang(x) for x in lang_files}
    
def getData(form, strings):
    date_time_str = f'{request.form["pizza_date"]} {request.form["pizza_time"]}'
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    return get_pizza_data(date_time_obj, strings, int(form["pizzas"]), int(form["sour_time"]), int(form["ferm_time"]), 
                int(form["rest_time"]), form["type"]=="original")

def locale_index(language="en"):
    t = datetime.now().replace(minute=0)+timedelta(hours=48)
    def_data = {"pizzas":6, "sour_time":8, "ferm_time":24, "rest_time":2, "pizza_date":t.strftime('%Y-%m-%d'), 'pizza_time':'12:00', 'type':'original'}
    data = get_pizza_data(t, strings=langs[language])
    return render_template("index.html", data=data, form_data=def_data, strings=langs[language])

def locale_result(language="en"):
    return render_template("index.html", data=getData(request.form, strings=langs[language]), form_data=request.form, strings=langs[language])

@app.route("/")
def index():
    return locale_index()

@app.route("/", methods=['POST'])
def index_post():
    return result('en')

@app.route("/<language>", methods=['POST'])
def result(language):
    return locale_result(language)

@app.route("/<language>")
def set_lang(language):
    return locale_index(language)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)