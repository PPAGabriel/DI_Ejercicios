import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    ciudad = "Vigo"
    return render_template('index.html',lugar=ciudad)


@app.route('/hola')
def hola():
    minumero=random.randint(0, 10)
    return "Hola mundo! "+str(minumero)

@app.route('/<int:numero>')
def numero_cualquiera(numero):
    multiplicado=numero*10
    return str(multiplicado)

if __name__ == '__main__':
    app.run()
