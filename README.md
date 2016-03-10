Fullstack Project #2: Tournament

Files for use are located within vagrant/tournament:
- tournament.py
- tournament.sql
- tournament_test.py

Required to run program:
- vagrant
- virtual box
- PostgreSQL

Instructions:
1. Clone repo
2. Open a new terminal window and enter the following:
3. $ cd fullstack
4. $ cd vagrant
5. $ vagrant up
6. $ vagrant ssh
7. $ cd /vagrant/tournament
8. Once vagrant is up and running you will need to connect to the database
  with: vagrant => \c tournament
9. Include the tournament.sql file with: vagrant => \i
##From here you can enter psql queries directly from the terminal window####
##Try running the following:
10. vagrant => INSERT INTO TABLE players(name) VALUES('Your name');
11. vagrant => SELECT * FROM players;


***To run tournament_test.py******
1. Open a new terminal window and enter the following:
2. $ cd fullstack
3. $ cd vagrant
4. $ cd vagrant ssh
5. cd vagrant/tournament
6. $ python tournament_test.py

You will see the following output:
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
0
1. countPlayers() returns 0 after initial deletePlayers() execution.
1
2. countPlayers() returns 1 after one player is registered.
2
3. countPlayers() returns 2 after two players are registered.
0
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
(33, 'Pinkie Pie')
(31, 'Fluttershy')
(33, 'Pinkie Pie', 31, 'Fluttershy')
(34, 'Rarity')
(37, 'Princess Luna')
(34, 'Rarity', 37, 'Princess Luna')
(32, 'Applejack')
(30, 'Twilight Sparkle')
(32, 'Applejack', 30, 'Twilight Sparkle')
(36, 'Princess Celestia')
(35, 'Rainbow Dash')
(36, 'Princess Celestia', 35, 'Rainbow Dash')
(36, 'Princess Celestia')
(32, 'Applejack')
(36, 'Princess Celestia', 32, 'Applejack')
(33, 'Pinkie Pie')
(34, 'Rarity')
(33, 'Pinkie Pie', 34, 'Rarity')
(35, 'Rainbow Dash')
(37, 'Princess Luna')
(35, 'Rainbow Dash', 37, 'Princess Luna')
(30, 'Twilight Sparkle')
(31, 'Fluttershy')
(30, 'Twilight Sparkle', 31, 'Fluttershy')
10. After one match, players with one win are properly paired.
Success!  All tests pass!