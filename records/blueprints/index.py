from . import index_blue


@index_blue.route('/')
@index_blue.route('/index')
@index_blue.route('/home')
def index_page():
    return 'index_page'
