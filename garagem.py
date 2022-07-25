from flask import jsonify, Request, request
from flask import Flask
import uuid


app = Flask(__name__)

garagem = []

@app.route("/entrada/carros", methods=['POST']) #cadastra o carro na hora da entrada
def cadastrar():
    motorista = request.json 
    for carro in garagem:
        if carro["carro"] == motorista["carro"] and carro["placa"] == motorista["placa"]:  
            return {"status":"Cliente já existe."}
    motorista = {
        "id": str(uuid.uuid4()),
        "carro": motorista["carro"],
        "placa": motorista["placa"]
        }
    garagem.append(motorista)
    return jsonify(motorista)

@app.route("/entrada/plano", methods=['POST']) #verifica se o carro se encontra na garagem
def comunicação():
    pacote_mensal = request.json
    for carros_vip in garagem:
        if carros_vip["carro"] == pacote_mensal["carro"] and carros_vip["placa"] == pacote_mensal["placa"]:
            return{"status":"carro na garagem."}
        else:
            return{"Status":"Carro não está dentro da garagem."}

@app.route("/dentro/garagem") #mostra todos os carros que estão dentro da garagem
def garagem():
    return jsonify(garagem)

@app.route("/excluir/carros", methods=['POST']) #deleta os carros da garagem
def desligar():
    body_excluir = request.json
    print(garagem)
    for dell in garagem:
        if dell["id"] == body_excluir["id"]:
            plano_vip.remove(dell)
            return body_excluir
plano_vip = []

@app.route("/venda/plano/vip", methods=['POST']) #vende o pacote mensal vip
def carageiro():
    pacote_vip = request.json 
    for plano in plano_vip:
        if plano["vip"] == pacote_vip["vip"]: 
            return {"status":"carro já incluso no Vip."}
    pacote_vip = {
        "id": str(uuid.uuid4()),
        "vip": pacote_vip["vip"]
        }
    plano_vip.append(pacote_vip)
    return jsonify(pacote_vip)

@app.route("/carrosvips") #mostra todos os carros que tem vip
def vip():
    return jsonify(plano_vip)

@app.route("/excluir/vips", methods=['POST']) # deleta os vips
def desligar():
    body_excluir = request.json
    print(plano_vip)
    for estoque in plano_vip:
        if estoque["id"] == body_excluir["id"]:
            plano_vip.remove(estoque)
            return body_excluir


app.run()