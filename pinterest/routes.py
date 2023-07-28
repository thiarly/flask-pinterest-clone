# criar as rotas do nosso site (os links)

from flask import Flask, render_template, url_for, redirect, flash
from pinterest import app, bcrypt, database
from flask_login import login_required, login_user, logout_user, current_user
from pinterest.forms import FormLogin, FormCriarConta
from pinterest.models import Usuario


@app.route("/", methods=["GET", "POST"])
def homepage():
    print("Homepage function called")  # Esta linha vai imprimir uma mensagem quando a função homepage for chamada
    form_login = FormLogin()
    if form_login.validate_on_submit():
        print('Form validado')
    
        
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario:
            print("Usuario encontrado: ", usuario.usuario)  # Esta linha vai imprimir o nome de usuário se um usuário for encontrado
            if bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
                print('Usuário e senha corretos')
                login_user(usuario)
                print("Usuario atual: ", current_user.usuario)  # Esta linha vai imprimir o nome de usuário do usuário logado
            
                return redirect(url_for("perfil", usuario=usuario.usuario))
        else:
            print("Usuario nao encontrado")  # Esta linha vai imprimir uma mensagem se nenhum usuário for encontrado
    else:
        print("Formulario nao validado", form_login.errors)  # Esta linha vai imprimir uma mensagem se o formulário não for validado
    
    return render_template("homepage.html", formlogin=form_login)



@app.route("/criar-conta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data).decode("utf-8")
        usuario = Usuario(email=form_criarconta.email.data, usuario=form_criarconta.usuario.data, senha=senha)
        
        database.session.add(usuario)
        database.session.commit()        
        flash("Conta criada com sucesso!", "success")
        login_user(usuario, remember=True)
                
        return redirect(url_for("perfil", usuario=usuario.usuario))
     
    return render_template("criar-conta.html", formcriarconta=form_criarconta)


@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))
