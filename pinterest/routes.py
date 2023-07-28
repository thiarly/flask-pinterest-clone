# criar as rotas do nosso site (os links)

from flask import Flask, render_template, url_for
from pinterest import app, bcrypt, database
from flask_login import login_required
from pinterest.forms import FormLogin, FormCriarConta
from pinterest.models import Usuario


@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    return render_template("homepage.html", formlogin=form_login)


@app.route("/criar-conta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data).decode("utf-8")
        usuario = Usuario(usuario=form_criarconta.usuario.data,
                          email=form_criarconta.email.data, senha=senha)
        
        database.session.add(usuario)
        database.session.commit()   
    
    return render_template("criar-conta.html", formcriarconta=form_criarconta)


@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
