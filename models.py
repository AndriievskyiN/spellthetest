from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class AllWords(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    theword = db.Column(db.String(10000))

class AllAnswer(db.Model):
    ans_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    word = db.Column(db.String(10000))
    user_answer = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class CorrectAnswer(db.Model):
    cor_ans_id = db.Column(db.Integer, primary_key=True)
    user_answer = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class IncorrectAnswer(db.Model):
    inc_ans_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(10000))
    user_answer = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
    notes = db.relationship('CorrectAnswer')