from flask import Flask
from src.routes import entidades;

app = Flask(__name__)

def init_app():
    app.register_blueprint(entidades.main, url_prefix='/api/entidades')
    return app