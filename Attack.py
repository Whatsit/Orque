""" Attack Module
"""
from random import randint

def attack(self, p1, p2):
	""" attack
	rolls random int [0,1] and returns winning player

	Parameters:
	p1 (player) - player1
	p2 (player) - player2
	
	Returns: (player) - winning player
	"""
    var = randint(0,1)
    if var == 0:
        return p1
    else:
        return p2
