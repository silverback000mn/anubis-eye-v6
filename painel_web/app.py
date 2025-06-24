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
