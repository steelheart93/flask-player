from flask import Flask, render_template, request, url_for, redirect, jsonify
from requests import get
from os import listdir, system
from random import shuffle

musicdir = listdir('static/audio/')
shuffle(musicdir)

app = Flask(__name__)


def consultar(idx):
    url = "http://www.bing.com/HPImageArchive.aspx"
    args = {'format': 'js', 'n': '1', 'idx': idx}

    try:
        response = get(url, params=args)

        if response.status_code == 200:
            response_json = response.json()
            images = response_json['images']
            urlbase = images[0]['urlbase'] + "_1366x768.jpg"
            bing = "https://www.bing.com" + urlbase
            derechos = images[0]['copyright']

            return idx, bing, derechos
        else:
            return [0, "/static/img/placeholder.png", "No Image Available"]
    except:
        return [0, "/static/img/placeholder.png", "No Image Available"]


@app.route('/')
def zero():
    return redirect(url_for('home', index=0, idx=0))


@app.route('/folder')
def folder():
    system('thunar static/audio/')
    return jsonify({"respuesta": "Carpeta Abierta"})


@app.route('/song/<index>/image/<idx>')
def home(index, idx):
    index = int(index)
    title = musicdir[index]
    imagen = consultar(idx)
    return render_template('index.html', titulo=title, idx=imagen[0], bing=imagen[1], derechos=imagen[2], i=index)


@app.route('/reload/<index>/<idx>')
def reload(index, idx):
    idx = int(idx)

    if idx < 7:
        idx = idx + 1
    else:
        idx = 0

    return redirect(url_for('home', index=index, idx=idx))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
