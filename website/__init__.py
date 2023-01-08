from flask import Flask
from .env import app_secret_key

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = app_secret_key

    from .views import views

    app.register_blueprint(views, url_perfix='/')
    
    return app


