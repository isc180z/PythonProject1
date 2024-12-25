from random import *

def shell_game():
    shells = ['A','B','C']
    input("Welcome to the shells game, I'll give you two tries to find in which shell i hid the key.")
    turn = 1
    while turn <= 2:
        winning_shell = choice(shells)
        input(f"You have {3-turn} tries left")
        chosen_shell = input("Which shell do you choose? A, B, or C?")
        while chosen_shell.upper() not in shells:
            chosen_shell = ("Choose a shell between A, B, or C")
        if chosen_shell.upper() == winning_shell:
            input("Great job, there was indeed a key under this shell !! You can leave with it :D")
            return True
        else:
            if turn == 1:
                input("There was no key under this shell... But you have another try, the key will hide somewhere else, good luck !")
            else:
                input(f"You're wrong ;) The key is in the {winning_shell} shell. Better luck next time.")
                return False
        turn += 1

def roll_dice_game():
    i = 1
    input("This is the dice game, you and the game master will roll a dice three times, the first one that rolls a six wins")
    while i <= 3:
        input(f"Roll the dice by pressing enter, you have {4-i} tries left.")

        player_roll = (randint(1, 6),randint(1, 6))
        print(f"You rolled {player_roll[0]} and {player_roll[1]}.")
        if player_roll[0] == 6 or player_roll[1] == 6 :
             print("You won the game, you get a key as reward !!")
             return True

        gm_roll = (randint(1, 6), randint(1, 6))
        print(f"The game master rolled {gm_roll[0]} and {gm_roll[1]}.")
        if gm_roll[0] == 6 or gm_roll[1] == 6:
            print("The game master won...")
            return False

        print("No 6 was rolled, the next turn will proceed.")

        i += 1

    print("No one rolled a 6 in 3 turns, it's a drawroll_.")
    return False



def chance_challenge():
    challenges = [shell_game,roll_dice_game]
    challenge = choice(challenges)
    print(challenge())