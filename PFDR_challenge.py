import json
import random
def load_riddles(file):
    with open(file,"r") as f:
        rids = json.load(f)
    return rids
def pere_fouras_riddles():
    rids = load_riddles("PFRiddles.json")
    rid = random.choice(rids)
    while rid["type"] != "Key":
        rid = random.choice(rids)
    attempt = 3
    while attempt > 0:
        print("Riddle: ", rid["question"])
        answer = str(input("Enter your answer: ")).lower()
        if answer == rid["answer"].lower():
            print("Correct! You win a key")
            return True
        attempt -= 1
        if attempt > 0:
            print("Wrong! You have ", attempt, "attempts left")
        else:
            print("You lost the game, the answer was: ", rid["answer"])
            return False
