from flask import Flask, render_template
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

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
            data = {
                "nome": nome,
                "status": "🔴 Inativa",
                "timestamp": "-"
            }
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
                    with open(os.path.join(caminho, arquivo), "r") as f:
                        try:
                            conta = json.load(f)
                            lista.append(conta)
                        except:
                            continue
        todas_contas[titulo] = lista

    return render_template("painel.html", status=status_list, todas_contas=todas_contas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
