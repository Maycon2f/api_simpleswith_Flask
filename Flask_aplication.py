from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/informacoes/')
def get_informacoes():
    informacoes = [
    {'id': 1, 'nome': 'Saci', 'idade': '25', 'cidade': 'Canoas', 'pais': 'Brasil'},
    {'id': 2, 'nome': 'joazinho', 'idade': '18', 'cidade': 'alagoas', 'pais': 'Brasil',},
    {'id': 3, 'nome': 'carlinhos', 'idade': '50', 'cidade': 'jacarépagua', 'pais': 'Brasil'}
    ]
    return jsonify(informacoes)




@app.route('/api/encontrar-info')
def encontrar_informacoes():
    details = {'id': 2, 'nome': 'joãozinho', 'idade': '18', 'cidade': 'alagoas', 'pais': 'Brazil'}
    return details

app.run




