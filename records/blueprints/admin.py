from flask import Blueprint, render_template


admin_blue = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blue.route('/')
def adminLogin_page():
    return 'adminLogin_page'


@admin_blue.route('/edit')
def adminEdit_page():
    return render_template('adminEdit-page/index.html')


@admin_blue.route('/edit/diary')
def editDiary_page():
    return render_template('adminEdit-page/diary/index.html')


@admin_blue.route('/edit/note')
def editNote_page():
    return render_template('adminEdit-page/note/index.html')


@admin_blue.route('/edit/idea')
def editIdea_page():
    return render_template('adminEdit-page/idea/index.html')


@admin_blue.route('/edit/link')
def editLink_page():
    return render_template('adminEdit-page/link/index.html')
