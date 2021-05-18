from app import db, Players

db.drop_all()
db.create_all()

Stephen = Users(id= 1,new_elo = 1500, wins = 4, loses =1, alliance = "Seraphon", name = "Stephen") # Extra: this section populates the table with an example entry
Colin = Users(id= 2,new_elo = 1600, wins = 5, loses =0, alliance = "Daughters of Khaine", name = "Colin")
Neil = Users(id= 3,new_elo = 1400, wins = 6, loses =4, alliance = "Slaanesh", name = "Neil")
David = Users(id= 4,new_elo = 800, wins = 1, loses =9, alliance = "Vampires", name = "David")

db.session.add(Stephen)
db.session.add(Colin)
db.session.add(Neil)
db.session.add(David)

db.session.commit()