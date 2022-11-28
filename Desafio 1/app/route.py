from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")


@app.route("/contato")
def contatos():
    return render_template("contato.html")

