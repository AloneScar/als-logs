# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Diary(db.Model):
    __tablename__ = 'diaries'

    picUrl = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    picName = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    type = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    belong = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    emotion = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    weather = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    by = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    dateCreated = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    dateUpdated = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    shortText = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    textUrl = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    snowId = db.Column(db.Text(collation='utf8_bin'), nullable=False)



class Idea(db.Model):
    __tablename__ = 'ideas'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    textUrl = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    type = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    snowId = db.Column(db.Text(collation='utf8_bin'), nullable=False)



class Link(db.Model):
    __tablename__ = 'links'

    imgUrl = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    href = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    belong = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    time = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    title = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    snowId = db.Column(db.Text(collation='utf8_bin'), nullable=False)



class Note(db.Model):
    __tablename__ = 'notes'

    picUrl = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    picName = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    type = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    belong = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    by = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    dateCreated = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    dateUpdated = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    shortText = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    textUrl = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    snowId = db.Column(db.Text(collation='utf8_bin'), nullable=False)



class Time(db.Model):
    __tablename__ = 'times'

    snowId = db.Column(db.Text(collation='utf8_bin'), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text(collation='utf8_bin'), nullable=False)
