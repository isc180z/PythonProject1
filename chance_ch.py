from random import *

def shell_game():
    shells = ['A','B','C']
    print('')


def chance_challenge():
    challenges = ['shell_game','roll_dice_game']
    challenge = choice(challenges)
    print(challenge())