"""Attack"""
from random import randint

"""attack() Peramiters: p1, p2
p1 = player1
p2 = player2
rolls random int [0,1] and returns winning player
"""
def attack(self, p1, p2):
    var = randint(0,1)
    if var == 0:
        return p1
    else:
        return p2
