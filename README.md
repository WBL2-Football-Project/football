# Football Tournament Tracker

## Github Setup
**These instructions apply to `git bash`**

* Clone repo into local directory using `git clone https://github.com/WBL2-Football-Project/football`

* Everytime you open your local project run the command `git pull` this will get any updates other members have made

* When uploading changes to the project use `git commit -a -m "Change Notes"` then `git push` to publish changes to the repo.

* For pushing to a new branch first use `git checkout <branch-name>` to switch branch or `git checkout -b <branch-name>` to create a new branch. Then use `git push origin <branch-name>` to push changes to specific branch.

## Project Set-up

1. Install all required libraries being used in the project by running `pip install -r requirements.txt`

## Outline of Project

The application supports football tournaments, allowing the referee to define the teams participating in the tournament, enter live statistics of the games and present the results to other users in real time. 

The application only supports one tournament at a time. Once the tournament is over (all matches have been played), the referee can reset all data and enter definitions for a new tournament. 

The application allows two different types of users to be entered: referees and other users. The referees define the tournaments and also have the possibility to enter current data related to the matches played, while the users only have the possibility to view the current results through it. 

The tournament involves 16 football teams playing matches in the first phase in group mode, with the winning teams then continuing in the knockout phase. In the group phase, teams are drawn into 4 groups of 4 teams each. There are 3 matches in each group, so that each team in the group plays 1 match against each of the others. In this way, 8 teams are selected, which then compete in the knock-out phase. 

During group play, the winning team receives 3 points, the losing team 0 and in the event of a draw, both teams receive 1 point each. Goals scored, goals lost and yellow cards received by the players of a team are also counted. At the end of the group games, the order of the groups is determined according to the following rules: 

- Greater number of points gained 

- If the number of points gained is the same, whoever who has more goals 

- If both the number of points and goals are equal, then the decision is made based on the amount of yellow cards 

- In the unlikely situation that all statistics match, a bespoke exception will display a message confirming that the referee is to make the decision themselves. 

The order and dates of all matches are drawn before the first game. One rule in particular is important, the team that has won its group is automatically pitted against the team that came second in another group in the knock-out phase. 

In the group phase there are 2 matches among the teams in the same group each day - for a total of 6 consecutive days. 

In the knock-out phase, the losing team is eliminated from the tournament and only the winner moves on. Thus, the following series of matches takes place in pairs: quarter-finals (4 out of 8 teams go through), semi-finals (2 out of 4 teams go through) and finals (the 2 best teams play the championship match and the 2 losers of the semi-finals play the match for 3rd place in the tournament). 

The quarter-final matches take place 2 days apart from the end of the group phase and occupy 2 consecutive days with 2 matches each. 

If a match in the knockout phase ends in a draw in regulation time, then the referee will call extra time (2x15 min) and then, if there is still a draw - the winner is determined by penalty shoot-outs. In the knockout phase, each match must ultimately determine a winner. 

The semi-final matches take place 2 days apart from the end of the quarter-final phase and occupy another 2 days, this time with 1 match each. 

The final matches take place 2 days apart from the end of the semi-final phase, on two consecutive days - first the 3rd place match of the tournament is played and then the championship match. 

The initial operation of the application, in which there is no data, starts with the definition of the first user - who automatically becomes the first referee. The referee has higher access rights to the application: he can change the status of other users by determining whether they are 'referees' or 'normal users'. The application should automatically block attempts to change the last existing 'judge' in the database to 'user', so that there is always one 'judge' left in the user list. In addition, "referees" have the right to define and modify all teams, they can save data on completed matches, they can call the function to draw matches between teams once (before the tournament starts) and they can call the function to reset the application data to the start level (no users, no teams, no data) at any time during the tournament.  

Other users only have access to view the tournament statistics in two modes: presentation of group phase statistics and the knock-out phase. 