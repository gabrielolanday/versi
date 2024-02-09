from flask import Flask
from flask_cors import CORS
from app.routes.routes import init_routes

def create_app():
    app = Flask(__name__)
    init_routes(app)
    CORS(app)
    return app
