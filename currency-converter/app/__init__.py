from flask import Flask
import os

def create_app():
    app_dir = os.path.abspath(os.path.dirname(__file__))  # directory of the app module
    template_dir = os.path.join(app_dir, '../templates')  # path to the templates directory
    app = Flask(__name__, template_folder=template_dir)

    from .routes import main
    app.register_blueprint(main)

    return app
