from flask import Flask, render_template, request, redirect
import os
import json
from datetime import datetime
from faker import Faker
import uuid
import subprocess
import signal

app = Flask(__name__)

# LOGIN E 2FA
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "anubis"
CODIGO_2FA = "8429"

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

    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        return render_template("verificar.html")
    else:
        return "Usuário ou senha inválidos.", 403

@app.route("/painel", methods=["POST", "GET"])
def painel():
    if request.method == "POST":
        codigo = request.form.get("codigo")
        if codigo != CODIGO_2FA:
            return "Código incorreto", 403

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

    # CONSELHO IA
    conselho_feedback = []
    try:
        with open("dados/conselho_feedback.json", "r") as f:
            conselho_data = json.load(f)
            conselho_feedback = conselho_data.get("sugestoes", [])
    except:
        pass

    return render_template("painel.html", status=status_list, todas_contas=todas_contas, conselho=conselho_feedback)

# NOVA CONTA
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

# CONTROLE DE IAs
@app.route("/controle_ia/<nome>/<acao>", methods=["POST"])
def controle_ia(nome, acao):
    pid_path = f"processos/{nome}.pid"

    if acao == "ativar":
        if os.path.exists(pid_path):
            return f"{nome} já está ativa."

        script = {
            "IA_RA": "ia/ra/ra.py",
            "IA_Isis": "ia/isis/isis.py",
            "IA_Sauron": "ia/sauron/sauron.py",
            "IA_Tempo": "ia/tempo/tempo.py",
            "HORUS": "horus_core.py",
            "Watchdog": "watchdog.py"
        }.get(nome)

        if not script:
            return "Script não encontrado.", 404

        proc = subprocess.Popen(["python", script])
        with open(pid_path, "w") as f:
            f.write(str(proc.pid))

        return redirect("/painel")

    elif acao == "desativar":
        if os.path.exists(pid_path):
            with open(pid_path, "r") as f:
                pid = int(f.read())
            try:
                os.kill(pid, signal.SIGTERM)
                os.remove(pid_path)
            except:
                pass

        return redirect("/painel")

    else:
        return "Ação inválida", 400

# API PARA ATUALIZAÇÃO AUTOMÁTICA
@app.route("/api/status")
def api_status():
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
    return json.dumps(status_list, ensure_ascii=False)

@app.route("/api/conselho")
def api_conselho():
    try:
        with open("dados/conselho_feedback.json", "r") as f:
            conselho_data = json.load(f)
            return json.dumps(conselho_data.get("sugestoes", []), ensure_ascii=False)
    except:
        return json.dumps([])

@app.route("/api/contas")
def api_contas():
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
    return json.dumps(todas_contas, ensure_ascii=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
