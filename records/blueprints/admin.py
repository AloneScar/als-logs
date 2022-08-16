from flask import Blueprint, render_template, request
import json


admin_blue = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blue.route('/')
def adminLogin_page():
    return 'adminLogin_page'


@admin_blue.route('/edit')
def adminEdit_page():
    return render_template('adminEdit-page/index.html')


@admin_blue.route('/edit/diary', methods=['GET', 'POST'])
def editDiary_page():
    if request.method == 'GET':
        return render_template('adminEdit-page/diary/index.html')
    else:
        data = json.loads(request.get_data())
        print(data['text'])
        return 'true'


@admin_blue.route('/edit/note')
def editNote_page():
    return render_template('adminEdit-page/note/index.html')


@admin_blue.route('/edit/idea')
def editIdea_page():
    return render_template('adminEdit-page/idea/index.html')


@admin_blue.route('/edit/link')
def editLink_page():
    return render_template('adminEdit-page/link/index.html')
