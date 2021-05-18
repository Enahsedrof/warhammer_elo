from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = '' # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # create SQLALchemy object

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    new_elo = db.Column(db.Float, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    loses = db.Column(db.Integer, nullable=False)
    alliance = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)

if __name__ == "__main__":
    app.run(debug=True)