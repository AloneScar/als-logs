from flask import Blueprint

admin_blue = Blueprint('admin', __name__, url_prefix='/admin')
home_blue = Blueprint('index', __name__, url_prefix='/')

from . import admin, home