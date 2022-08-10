# coding: utf-8
from sqlalchemy import Column, Text
from sqlalchemy.dialects.mysql import INTEGER, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Diary(Base):
    __tablename__ = 'diaries'

    picUrl = Column(TEXT, nullable=False)
    picName = Column(TEXT, nullable=False)
    id = Column(INTEGER, primary_key=True)
    title = Column(TEXT, nullable=False)
    type = Column(Text(collation='utf8_bin'), nullable=False)
    belong = Column(TEXT, nullable=False)
    emotion = Column(TEXT, nullable=False)
    weather = Column(TEXT, nullable=False)
    by = Column(TEXT, nullable=False)
    dateCreated = Column(TEXT, nullable=False)
    dateUpdated = Column(TEXT, nullable=False)
    shortText = Column(TEXT, nullable=False)
    textUrl = Column(TEXT, nullable=False)


class Idea(Base):
    __tablename__ = 'ideas'

    id = Column(INTEGER, primary_key=True)
    time = Column(TEXT, nullable=False)
    textUrl = Column(TEXT, nullable=False)


class Link(Base):
    __tablename__ = 'links'

    imgUrl = Column(Text(collation='utf8_bin'), nullable=False)
    href = Column(Text(collation='utf8_bin'), nullable=False)
    id = Column(INTEGER, primary_key=True)
    type = Column(TEXT, nullable=False)
    belong = Column(TEXT, nullable=False)
    time = Column(TEXT, nullable=False)
    title = Column(TEXT, nullable=False)


class Note(Base):
    __tablename__ = 'notes'

    picUrl = Column(TEXT, nullable=False)
    picName = Column(TEXT, nullable=False)
    id = Column(INTEGER, primary_key=True)
    title = Column(TEXT, nullable=False)
    type = Column(TEXT, nullable=False)
    belong = Column(TEXT, nullable=False)
    by = Column(TEXT, nullable=False)
    dateCreated = Column(TEXT, nullable=False)
    dateUpdated = Column(TEXT, nullable=False)
    shortText = Column(TEXT, nullable=False)
    textUrl = Column(TEXT, nullable=False)
