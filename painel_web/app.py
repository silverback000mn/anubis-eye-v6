from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "ciberpunk_key_2025"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["usuario"] == "admin" and request.form["senha"] == "anubis":
            session["auth"] = True
            return redirect("/verificar")
    return render_template("login.html")

@app.route("/verificar", methods=["GET", "POST"])
def verificar():
    if not session.get("auth"): return redirect("/login")
    if request.method == "POST":
        if request.form["token"] == "8429":
            session["logado"] = True
            return redirect("/")
    return render_template("verificar.html")

@app.route("/")
def home():
    if not session.get("logado"): return redirect("/login")

    try:
        with open("logs/supremos/horus.log", "r") as f:
            logs = f.readlines()
    except:
        logs = ["[HORUS] Nenhum log ainda."]

    return render_template("painel.html", logs=logs)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    import json

@app.route("/logs")
def exibir_logs():
    with open("logs/sistema_logs.json") as f:
        dados = json.load(f)
    return render_template("logs.html", logs=dados["logs"])

