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
        profession = input("And what is your use in today's society\n")
        if not definedleader:
            Leader = input("Will you be your team's leader ? This means a lot of responsibilities, answer with yes or no\n")
            Leader = Leader.lower()
            if Leader != "yes" and Leader != "no":
                print("I really wonder if I should let you in... The challenges didn't event begin and yet you've already failed answering a YES NO QUESTION")
                Leader = input("Come on, caps don't even matter...\n")
                Leader = Leader.lower()

compose_equipe()

input("test")
print("works")
input("test")
print("workéseful")
input("test")
print("possesed")
input("test")
