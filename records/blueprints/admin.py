from . import admin_blue


@admin_blue.route('/')
def adminLogin_page():
    return 'adminLogin_page'
