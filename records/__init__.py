from .blueprints import admin_blue
from .blueprints import index_blue
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)
db.create_all()


app.register_blueprint(index_blue)
app.register_blueprint(admin_blue)
