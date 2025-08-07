from flask import Flask
from app.routes import main as main_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    CORS(app)  # 🔥 This allows frontend requests
    return app

