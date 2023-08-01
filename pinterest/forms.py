# criar os formulários do nosso site

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from pinterest.models import Usuario

class FormLogin (FlaskForm):
    email = StringField("Usuario", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=10, message="A senha deve ter entre 6 e 10 caracteres")])
    botao_confirmacao = SubmitField("Fazer Login")
    
    # como coloquei unique=true no banco de dados, preciso verificar se o usuario ou email já existem
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("O e-mail não está cadastrado, faça seu cadastro.")
        
    
class FormCriarConta (FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    usuario = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=10, message="A senha deve ter entre 6 e 10 caracteres")])
    confirmacao_senha = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("senha", message="As senhas devem ser iguais")])
    botao_confirmacao = SubmitField("Criar Conta")
    
    # como coloquei unique=true no banco de dados, preciso verificar se o usuario ou email já existem
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("O e-mail já está cadastrado")
    
    def validate_usuario(self, usuario):
        usuario = Usuario.query.filter_by(usuario=usuario.data).first()
        if usuario:
            raise ValidationError("O nome de usuário já está cadastrado")
    
    
    
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")