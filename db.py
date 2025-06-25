import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

class Db:
    def __init__(self):
        self.db = SQLAlchemy()

    def init_app(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
        self.db.init_app(app)