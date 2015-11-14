"""Attack"""
from random import randint

def attack(self, p1, p2):
    """attack() Peramiters: p1, p2
    p1 = player1
    p2 = player2
    rolls random int [0,1] and returns winning player
    """
    var = randint(0,1)
    if var == 0:
        return p1
    else:
        return p2
