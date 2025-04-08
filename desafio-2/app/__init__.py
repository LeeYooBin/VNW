from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .extensions import db
from .routes import bp
import os

def create_app():
  load_dotenv()

  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  db.init_app(app)
  app.register_blueprint(bp)

  CORS(app)

  return app
