# criar as rotas do nosso site (os links)

from flask import Flask, render_template, url_for
from pinterest import app
from flask_login import login_required
from pinterest.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", formlogin=formlogin)

@app.route("/criar-conta", methods=["GET", "POST"])
def criar_conta():
    formcriarconta = FormCriarConta()
    return render_template("criar-conta.html", formcriarconta=formcriarconta)


@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
