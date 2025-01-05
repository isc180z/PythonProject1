
from datetime import time

from math_ch import *

import utility_functions
from math_ch import *
from battleship import *
from chance_ch import *
from PFDR_challenge import *
from final_challenge import *
from utility_functions import introduction, compose_equipe, challenges_menu, choose_player


def game():
    introduction()
    team = compose_equipe()
    keys = 0
    while keys < 3:
        challenge_choice = challenges_menu()-1
        selected_player = choose_player(team)
        print("The game is starting")
        print("Loading...")
        time.sleep(2)
        challenges = [math_challenge(), battle_ship_game(), chance_challenge(), pere_fouras_riddles()]
        challenge = challenges[challenge_choice]
        res = challenge()
        if res:
            keys += 1

    print("Your team managed to win 3 keys !!")
    print("You will now face to final challenge, ")
    print("in this challenge we will give you clues to guess a word")
    print("if you guess the word correctly you win the game")
    print("otherwise, you lose the game")

    fc = treasury_room()
    if keys == 3 :
        if fc :
            print("Congratulations you have completed and won the game !!!")
        else :
            print("You lost the game...")

game()