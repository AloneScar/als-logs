from records.blueprints.admin import admin_blue
from records.blueprints.home import home_blue
from records.extensions import db


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('settings.py')

db.init_app(app)

app.register_blueprint(home_blue)
app.register_blueprint(admin_blue)
