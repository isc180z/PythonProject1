### Valentin

from random import choice
import json


def load_file(file):
    with open(file) as f:
        data = json.load(f)
    return data

def treasury_room():
    tv_game = load_file('Data/TRClues.json')

    year = choice(list(tv_game['Fort Boyard'].keys()))
    show = choice(list(tv_game['Fort Boyard'][year].keys()))
    clues = tv_game['Fort Boyard'][year][show]['Clues']
    code_word = tv_game['Fort Boyard'][year][show]['CODE-WORD']

    print("The first three clues are :\n")
    for i in clues[:3]:
        print("    -",i)

    answer_correct = False
    attempts = 3
    while attempts > 0 and answer_correct == False:
        answer = input("\nUsing these clues, what could be the code word?\n")
        if answer.upper() == code_word:
            answer_correct = True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts remaining, here's another hint.\n")
                for i in clues[:(3 + abs(attempts-3))]:
                    print("    -", i)
            else:
                print(f"You lost, the code word was {code_word}")
treasury_room()
