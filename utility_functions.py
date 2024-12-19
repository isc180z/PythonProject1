from random import *

def introduction():
    print("Welcome to the Fort Boyard where you will be stuck for an undefined amount of time.")
    print("Your goal is to complete complex challenges that even the wisest mind can't even begin to comprehend.")
    print("Solving these problems will give you a key, gather three of them and you'll be allowed to meet the Père Fouras.")
    print("Your spirits will need to be elevated to understand his riddles. But if you unearth all the answers, the door to the treasure room will open")

def compose_equipe():
    nbplayers = int(input("How many players will dare challenge my Forts mysteries?\n"))
    while nbplayers <= 0 or nbplayers > 3:
        if nbplayers < 0:
            print("Excuse-me ? Who are these 'negative people' you talk about? How are they even supposed to materialise ?")
            nbplayers = int(input("Stop trying to find bugs in my code, just give me a number between 1 and 3 (included)\n"))
        elif nbplayers == 0:
            print("Well then, you're allowed to come unaccompanied by yourself, but at least bring me one person")
            nbplayers = int(input("Please, someone...\n"))
        else:
            print("I'm sorry but you're not allowed to set foot in my abode with such a crowd")
            nbplayers = int(input("You shall be at most 3 minds\n"))




    players = []
    definedleader = False
    for i in range(nbplayers):
        players.append({})
        name = input(f"Player {i+1} What can I call you ?\n")
        players[i]['name'] = name
        profession = input(f"Great, {name}, what is your use in today's society\n")
        players[i]['profession'] = profession
        if not definedleader:
            if i == nbplayers - 1:
                definedleader = True
                print("You're the last one left, you must be the leader then.")
                players[i]['leader'] = True
            else:
                Leader = input("Will you be your team's leader ? This means a lot of responsibilities, answer with yes or no\n")
                Leader = Leader.lower()
                if Leader != "yes" and Leader != "no":
                    print("I really wonder if I should let you in... The challenges didn't event begin and yet you've already failed answering a YES NO QUESTION")
                    Leader = input("Come on, caps don't even matter...\n")
                    Leader = Leader.lower()
                if Leader == "yes" :
                    definedleader = True
                    print("Good, you will lead them through these challenges.\n")
                    players[i]['leader'] = True
                elif Leader == "no" :
                    print("Well if you don't wish to, I won't force you.\n")
                    players[i]['leader'] = False
        else:
            players[i]['leader'] = False
    return players

def challenges_menu():
    print("1. Mathematics challenge\n"
          "2. Logic challenge\n"
          "3. Chance challenge\n"
          "4. Père Fouras's riddle\n")
    answer = input("Which challenge would you like to do?\n")
    if answer == "1":
        x = randint(1,3)
    elif answer == "2":
        x = randint(1)
    elif answer == "3":
        x = randint(1,2)
    elif answer == "4":
        x = randint(1,)


def choose_player(team:list)->dict:
    for i in range(team):
        if team[i]['leader']:
            print(f"{i}, {team[i]['name']}, ({team[i]['profession']}) - Leader")
        else:
            print(f"{i}, {team[i]['name']}, ({team[i]['profession']}) - Member")
    thechosenone = input("Who will pass this test? Tell me the number of your desired player.\n")
    return team[thechosenone]
