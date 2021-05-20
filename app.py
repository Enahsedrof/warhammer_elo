from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.105.170.188/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config["SECRET_KEY"] = "ererhe"
db = SQLAlchemy(app) # create SQLALchemy object

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    alliance = db.Column(db.String(30), nullable=False)
    current_rating = db.Column(db.Integer, nullable=False)

class PlayersForm(FlaskForm):
    name = StringField("Player name")
    alliance = StringField("Player alliance")
    current_rating = IntegerField()
    submit = SubmitField("Add Player")

@app.route("/")
def index():
    player_list = Players.query.order_by(Players.current_rating.desc()).all()
    return render_template("index.html", player_list=player_list)

@app.route("/add", methods=["POST","GET"])
def add():
    form = PlayersForm()
    if form.validate_on_submit():
        new_player_list = Players(name=form.name.data, alliance=form.alliance.data, current_rating=form.current_rating.data)
        db.session.add(new_player_list)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)

@app.route("/win/<int:players_id>", methods=["POST","GET"])
def update(players_id):
    players = Players.query.filter_by(id=players_id).first()
    players.current_rating =  players.current_rating + 15
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:players_id>", methods=["POST","GET"])
def delete(players_id):
    players = Players.query.filter_by(id=players_id).first()
    db.session.delete(players)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')