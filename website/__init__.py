from flask import Flask
import os 

try:
    from .env import app_secret_key
except Exception:
    app_secret_key = None


def _get_secret_key():
    return (
        os.environ.get('APP_SECRET_KEY')
        or os.environ.get('FLASK_SECRET_KEY')
        or os.environ.get('SECRET_KEY')
        or app_secret_key
        or 'change-me-in-production'
    )

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = _get_secret_key()

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    return app


