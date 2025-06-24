from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "anubis"
CODIGO_2FA = "8429"

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/verificar", methods=["POST"])
def verificar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        return render_template("verificar.html")
    else:
        return "Login inválido", 403

@app.route("/painel", methods=["POST"])
def painel():
    codigo = request.form.get("codigo")

    if codigo == CODIGO_2FA:
        return render_template("painel.html")
    else:
        return "Código incorreto", 403

# ⬇️ ESSA PARTE É FUNDAMENTAL para rodar no Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    import json

@app.route("/logs")
def logs():
    try:
        with open("logs/sistema_logs.json", "r") as f:
            dados = json.load(f)
        return render_template("logs.html", logs=dados["logs"])
    except:
        return "Arquivo de logs não encontrado ou mal formatado.", 500
import os

@app.route("/contas")
def contas():
    base_dir = "contas"
    categorias = {
        "Contas Altas": "altas",
        "Contas Médias": "medias",
        "Contas Baixas": "baixas",
        "Contas Travadas": "crashou"
    }

    todas_contas = {}

    for nome, pasta in categorias.items():
        caminho = os.path.join(base_dir, pasta)
        lista = []

        if os.path.exists(caminho):
            for arquivo in os.listdir(caminho):
                if arquivo.endswith(".json"):
                    with open(os.path.join(caminho, arquivo), "r") as f:
                        try:
                            dados = json.load(f)
                            lista.append(dados)
                        except:
                            continue
        todas_contas[nome] = lista

    return render_template("contas.html", todas_contas=todas_contas)

