from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.197.238.11/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # create SQLALchemy object

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    alliance = db.Column(db.String(30), nullable=False)
    current_rating = db.Column(db.Integer, nullable=False)

    # new_elo = db.Column(db.Float, nullable=False)
    # wins = db.Column(db.Integer, nullable=False)
    # loses = db.Column(db.Integer, nullable=False)
    # alliance = db.Column(db.String(30), nullable=False)
    # name = db.Column(db.String(30), nullable=False)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')