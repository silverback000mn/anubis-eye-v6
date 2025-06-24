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
from faker import Faker
import uuid

faker = Faker("pt_BR")

@app.route("/nova_conta", methods=["GET", "POST"])
def nova_conta():
    if request.method == "GET":
        return render_template("nova_conta.html")
    
    usuario = request.form.get("usuario")
    email = request.form.get("email")
    senha = request.form.get("senha")
    classificacao = request.form.get("classificacao")

    if not usuario or not email or not senha or not classificacao:
        return "Campos obrigatórios faltando.", 400

    bio = faker.catch_phrase() + " " + faker.job()
    conta = {
        "usuario": usuario,
        "email": email,
        "senha": senha,
        "bio": bio,
        "classificacao": classificacao
    }

    pasta_destino = f"contas/{classificacao}s"
    os.makedirs(pasta_destino, exist_ok=True)
    arquivo = os.path.join(pasta_destino, f"{uuid.uuid4()}.json")

    with open(arquivo, "w") as f:
        json.dump(conta, f, indent=4, ensure_ascii=False)

    return f"✅ Conta criada com sucesso!<br><br><a href='/contas'>Ver contas</a>"

