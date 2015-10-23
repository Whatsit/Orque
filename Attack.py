from random import randint

# returns the winner of the fight
def attack(self, p1, p2):
    var = randint(0,1)
    if var == 0:
        return p1
    else:
        return p2
