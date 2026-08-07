import os
from flask import Flask
from config import Config

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_app(config_class=Config):
    app = Flask(
        __name__,
        template_folder=os.path.join(_BASE_DIR, 'templates'),
        static_folder=os.path.join(_BASE_DIR, 'static'),
    )
    app.config.from_object(config_class)

    from app import routes
    app.register_blueprint(routes.main)

    return app