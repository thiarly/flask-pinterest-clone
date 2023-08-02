from pinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

# sempre criar uma função load_usuario para o sistema de login
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String(100), nullable=False, unique=True)
    email = database.Column(database.String(50), nullable=False, unique=True)
    senha = database.Column(database.String(50), nullable=False)
    foto = database.relationship("Foto", backref="usuario", lazy=True)


class Foto(database.Model): 
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.jpg")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)
