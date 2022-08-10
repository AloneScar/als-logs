from . import home_blue
from flask import render_template
from . import models


@home_blue.route('/')
@home_blue.route('/index')
@home_blue.route('/home')
def index_page():
    return render_template('home-page/index.html')
