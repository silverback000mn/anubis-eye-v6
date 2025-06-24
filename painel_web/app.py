from flask import Flask, render_template, request, redirect
import os
import json
from datetime import datetime
from faker import Faker
import uuid

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

    # CONSELHO
    conselho_feedback = []
    try:
        with open("dados/conselho_feedback.json", "r") as f:
            conselho_data = json.load(f)
            conselho_feedback = conselho_data.get("sugestoes", [])
    except:
        pass

    return render_template("painel.html", status=status_list, todas_contas=todas_contas, conselho=conselho_feedback)

@app.route("/nova_conta_via_painel", methods=["POST"])
def nova_conta_via_painel():
    usuario = request.form.get("usuario")
    email = request.form.get("email")
    senha = request.form.get("senha")
    classificacao = request.form.get("classificacao")

    if not usuario or not email or not senha or not classificacao:
        return "Erro: preencha todos os campos.", 400

    fake = Faker("pt_BR")
    bio = fake.catch_phrase() + " — " + fake.job()

    conta = {
        "usuario": usuario,
        "email": email,
        "senha": senha,
        "bio": bio,
        "classificacao": classificacao
    }

    pasta_destino = f"contas/{classificacao}s"
    os.makedirs(pasta_destino, exist_ok=True)
    caminho = os.path.join(pasta_destino, f"{uuid.uuid4()}.json")

    with open(caminho, "w") as f:
        json.dump(conta, f, indent=4, ensure_ascii=False)

    return redirect("/painel")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
