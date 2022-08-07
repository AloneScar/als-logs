from flask import Blueprint

admin_blue = Blueprint('admin', __name__, url_prefix='/admin')
index_blue = Blueprint('index', __name__, url_prefix='/')

from . import admin, index
