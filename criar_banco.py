from pinterest import app, database
from pinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()