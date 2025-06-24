from flask import Flask, render_template, request, redirect
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/verificar", methods=["POST"])
def verificar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if usuario == "admin" and senha == "anubis":
        return redirect("/painel")
    return "Login inválido", 403

@app.route("/painel")
def painel():
    # STATUS DAS IAs
    nomes_ias = ["IA_RA", "IA_Isis", "IA_Sauron", "IA_Tempo", "HORUS", "Watchdog"]
    status_list = []
    for nome in nomes_ias:
        path = f"status/{nome}.status"
        try:
            with open(path, "r") as f:
                data = json.load(f)
        except:
            data = {"nome": nome, "status": "🔴 Inativa", "timestamp": "-"}
        status_list.append(data)

    # CONTAS
    categorias = {
        "Contas Altas": "altas",
        "Contas Médias": "medias",
        "Contas Baixas": "baixas",
        "Contas Travadas": "crashou"
    }
    todas_contas = {}
    for titulo, pasta in categorias.items():
        caminho = f"contas/{pasta}"
        lista = []
        if os.path.exists(caminho):
            for arquivo in os.listdir(caminho):
                if arquivo.endswith(".json"):
                    try:
                        with open(os.path.join(caminho, arquivo), "r") as f:
                            conta = json.load(f)
                            lista.append(conta)
                    except:
                        continue
        todas_contas[titulo] = lista

    # CONSELHO
    conselho = []
    conselho_path = "dados/conselho.json"
    if os.path.exists(conselho_path):
        with open(conselho_path, "r") as f:
            try:
                conselho = json.load(f)
            except:
                conselho = []

    return render_template("painel.html", status=status_list, todas_contas=todas_contas, conselho=conselho)

@app.route("/nova_conta_via_painel", methods=["POST"])
def nova_conta_via_painel():
    usuario = request.form.get("usuario")
    email = request.form.get("email")
    senha = request.form.get("senha")
    classificacao = request.form.get("classificacao")

    if not os.path.exists(f"contas/{classificacao}"):
        os.makedirs(f"contas/{classificacao}")

    conta = {
        "usuario": usuario,
        "email": email,
        "senha": senha,
        "classificacao": classificacao,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    nome_arquivo = f"contas/{classificacao}/{usuario}_{int(datetime.now().timestamp())}.json"
    with open(nome_arquivo, "w") as f:
        json.dump(conta, f, indent=4)

    return redirect("/painel")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
