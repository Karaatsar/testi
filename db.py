from os import getenv
from flask_sqlalchemy import SQLAlchemy
from app import app


database_url = getenv("DATABASE_URL", "postgresql:///ksatsar")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
