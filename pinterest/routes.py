# criar as rotas do nosso site (os links)

from flask import Flask, render_template, url_for, redirect, flash
from pinterest import app, bcrypt, database
from flask_login import login_required, login_user, logout_user, current_user
from pinterest.forms import FormLogin, FormCriarConta, FormFoto
from pinterest.models import Usuario, Foto
import os
from werkzeug.utils import secure_filename


@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        print('Form validado')
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario:
            if bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
                print('Usuário e senha corretos')
                login_user(usuario)
                return redirect(url_for("perfil", id_usuario=usuario.id))
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
                
        return redirect(url_for("perfil", id_usuario=usuario.id))
     
    return render_template("criar-conta.html", formcriarconta=form_criarconta)


@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            #salvar o arquivo na pasta static/image/fotos_post
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                              app.config["UPLOAD_FOLDER"], nome_seguro)
            print(caminho)
            arquivo.save(caminho)
            #registrar o arquivo no banco de dados
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
            
            
        return render_template("perfil.html", usuario=current_user, formfoto=form_foto)
    
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, formfoto=None)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))



@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all() #[:100]
    return render_template("feed.html", fotos=fotos)
