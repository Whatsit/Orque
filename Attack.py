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

	while(p1.health > 0 or p2.health > 0):
		varP1 = randint(p1.attackRange[0],p1.attackRange[1] + p1.attackBonus)
		varP2 = randint(p2.attackRange[0],p2.attackRange[1] + p2.attackBonus)
		res2 = varP1 - p2.protection
		if(res2 < 0):
			res2 = 0
		p2.health = p2.health - res2
		print("P1 action :: " + str(p2.health) + " :: -" + str(varP1) + " :: Resisted: " + str(res2))
		if(p2.health <= 0):
			return p1.name
		res1 = varP2 - p1.protection
		if(res1 < 0):
			res1 = 0
		p1.health = p1.health - res1
		print("P2 action :: " + str(p1.health) + " :: -" + str(varP2) + " :: Resisted: " + str(res1))
		if(p1.health <= 0):
			return p2.name
		print("---------------------------------------")
	return None
