""" Attack Module
"""
from random import randint

def attack(self, p1, p2):
<<<<<<< HEAD
	""" attack
	rolls random int [0,1] and returns winning player

	Parameters:
	p1 (player) - player1
	p2 (player) - player2
	
	Returns: (player) - winning player
	"""
=======
    """attack() Peramiters: p1, p2
    p1 = player1
    p2 = player2
    rolls random int [0,1] and returns winning player
    """
>>>>>>> refs/remotes/Whatsit/master
    var = randint(0,1)
    if var == 0:
        return p1
    else:
        return p2
