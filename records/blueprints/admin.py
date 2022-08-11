from flask import Blueprint

admin_blue = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blue.route('/')
def adminLogin_page():
    return 'adminLogin_page'
