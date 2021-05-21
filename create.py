from app import db, Players, Games

db.drop_all()
db.create_all()

Stephen = Players(id =1 ,name = "Stephen", alliance = "Seraphon", current_rating = 1000,  ) 
Colin = Players(id = 2,name = "Colin", alliance = "Daughters of Khaine", current_rating = 900 )
Neil = Players(id = 3,name = "Neil", alliance = "Slaanesh", current_rating = 1100 )
David = Players(id = 4,name = "David", alliance = "Vampires", current_rating = 1200 )

db.session.add(Stephen)
db.session.add(Colin)
db.session.add(Neil)
db.session.add(David)

db.session.commit()

Age_of_Sigmar = Games(id =1, game_type = "Age of Sigmar", players = Players.query.filter_by(name = "Neil").first())
db.session.add(Age_of_Sigmar)
db.session.commit()

