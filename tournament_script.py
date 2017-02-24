import random

from tournament import connect
from tournament import reportMatch

from tournament_test import deletePlayers


the_players = [
(1, 'Tofik'),
(2, 'Cathy'),
(3, 'Frank'),
(4, 'Alexa'),
(5, 'Lora')
]


def registerPlayerUpdate(player_id, name):
	"""Add a player to the tournament database.
	The database assigns a unique serial id number for the player.
	(This should be handled by our SQL database schema, not in your python code)
	Args:
		name: the player's full name (need not be unique)
	"""
	db = connect()
	db_cursor = db.cursor()
	query = "INSERT INTO players (id, name) VALUES (%s, %s)"
	db_cursor.execute(query, (player_id, name))
	db.commit()
	db.close


def createRandomMatches(player_list, num_matches):
	num_players = len(player_list)
	for i in xrange(num_matches):
		print 'match %s' % (i + 1)
		palyer1_index = random.randint(0, num_players - 1)
		palyer2_index = random.randint(0, num_players - 1)
		if palyer2_index == palyer1_index:
			palyer2_index = (palyer1_index + 1) % num_players
		winner_id = player_list[palyer1_index][0]
		winner_name = player_list[palyer1_index][1]
		loser_id = player_list[palyer2_index][0]
		loser_name = player_list[palyer2_index][1]
		reportMatch(winner_id, loser_id)
		print "%s (id=%s) beat %s (id=%s)" % (winner_name,
											  winner_id,
											  loser_name,
											  loser_id)


def setup_players_and_matches():
	deletePlayers()
	for player in the_players:
		registerPlayerUpdate(player[0], player[1])

	createRandomMatches(the_players, 100)

if __name__ == '__main__':
	setup_players_and_matches()
