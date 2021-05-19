ELO calculator (for warhammer)

** Inspired by this site ** http://aligulac.com/
This is very extensive but I would like to build from the ground up a similiar platform but for competitive tabletop gaming,
Very simply I will make up a handful of players and record fake matches to track their rating.
Once I have achieved that I will get the programming done and push out the frontend.
Finishing that I will then scale it up with real tournaments and people. (This is also a personal project so will be done even after the acad)
There is a website with results and look to pull results from that site.
Scale it up and record several years worth of data
Cry in sleep after that part is finished.

SQL database
- players and game results
- updates ELO based on results added
- run on Google cloud
- Start small and then worry about upscaling and adding features like recorded events and Faction played

HTML
- table showing ELO
- Compares 2 players and predicted result
- Allows matches to be entered??
-

Python
- runs the site
- implement results into DB



Project Management - 	JIRA
CI - 			Github
Programming - 		Python
Version control - 	git
CI Server - 		Jenkins
Unit Testing -		pytest
Integration Testing -	Selenium
Front End - 		HTML & CSS
DB - 			MySQL
Cloud - 		GCL



SQL -

Table one : used to store info on players

id
new_elo
wins
loses
alliance
name

Table 2 : used to update ELO based on match result

Opponent1
Opponent2
OP1_result
OP2_result
Update new_elo for both players,
old_elo

ELO is calculated based on who is predicted to win. If both players are evenly matched, they will get +- 10 points for a win/lose.
For the initial task every player will be assumed to be evenly matched.
Moving forward a more robust system for ELO can be used, e.g. a 2000 rated player vs an 1000 rated player would be a +1 or -20 for the 2000 player. Reversing for the 1000 player.

Next steps to improve on would be
- ranking every player and displaying that on a table. 
- Sorting by alliance and ranking within alliance
- Seperate ELO if a different alliance was used 
- Take into account Major/minor win/lose and secondaries 
- Table to represent events and the matches played therein
- Begin the absurd task of understanding the mathematcial function that is used for ELO.
- a function to enter two players and produce a predicted match result
