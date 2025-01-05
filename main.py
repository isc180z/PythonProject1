
from datetime import time

from math_ch import *


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
    i = 0
    challenges = [math_challenge, battle_ship_game, chance_challenge, pere_fouras_riddles]
    done_challenges = []
    while keys < 3 and i < 3:

        while challenges_menu() < len(challenges):
            challenge_choice = challenges_menu()-1
        selected_player = choose_player(team)
        print("The game is starting")
        print("Loading...")
        done_challenges.append(challenges[challenge_choice])
        challenge = challenges[challenge_choice]
        challenges.pop(challenge)
        res = challenge()
        if res:
            keys += 1
        i+=1

    print("Your team managed to win 3 keys !!")
    print("You will now face to final challenge, ")
    print("in this challenge we will give you clues to guess a word")
    print("if you guess the word correctly you win the game")
    print("otherwise, you lose the game")


    if keys == 3 :
        fc = treasury_room()
        if fc:
            print("Congratulations you have completed and won the game !!!")
        else :
            print("You lost the game...")
    else:
        print("You lost the game...")
game()