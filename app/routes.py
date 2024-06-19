from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome ='Alba'
    dados ={'profissão':'Professora','canal':'Prof Alba Lopes'}
    return render_template('index.html',dados = dados)

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')