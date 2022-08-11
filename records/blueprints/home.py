from flask import render_template, jsonify
from sqlalchemy.orm import class_mapper
from records.models import Diary, Note, Idea, Link
from flask import Blueprint
import json


home_blue = Blueprint('home', __name__, url_prefix='/')


@home_blue.route('/')
@home_blue.route('/index')
@home_blue.route('/home')
def index_page():
    return render_template('home-page/index.html')


@home_blue.route('/getHomeContents')
def getHomeContents():
    def model_to_json_test():
        q = db.session.query(WhiteSite).first()  # db = SQLAlchemy()
        q_dict = serialize(q)
        q_json = jsonify(q_dict)
        return q_json

    def serialize(model):
        columns = [c.key for c in class_mapper(model.__class__).columns]
        return dict((c, getattr(model, c)) for c in columns)
    aaa = Diary.query.all()
    # TODO arrange the two function, write the content sort by time
    # diaries = []
    # for i in aaa:
    #     diaries.append(i.json)
    return {'contents': [serialize(i) for i in aaa]}
