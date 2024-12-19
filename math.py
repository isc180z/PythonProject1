from random import *
f=0
def factorial(n):
    k=1
    if n==0:
        k=1
    else:
        for i in range(1,n+1):
            k=k*i
    return k

def math_challenge_factorial():
    n=randint(1,10)
    factorial(n)
    z=int(input("Enter your answer: "))
    if z==k:
        print("Correct! You win a key.")
    else:
        print("Incorrect!")


def math_roulette_challenge():
    list=[]
    op=["+","-","*"]
    for i in range(5):
        list.append(randint(1,20))
    o=choice(op)
    print(list)
    if o=="+":
        print("Compute the somme of the terms of this list")
        r=0
        for i in range(5):
            r=r+list[i]
    elif o=="-":
        print("Compute the difference of the terms of this list")
        r=list[0]
        for i in range(1,5):
            r=r-list[i]
    else:
        print("Compute the product of the terms of this list")
        r=1
        for i in range(5):
            r=r*list[i]
    a=int(input("Enter your answer: "))
    if a==r:
        print("Correct answer! You win a key")
    else:
        print("You lose !")