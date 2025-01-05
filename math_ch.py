### Isaac

import random
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
    n=random.randint(1,10)
    k = factorial(n)
    z=int(input(f"Compute the factorial of {n}: "))
    if z==k:
        print("Correct! You win a key.")
        return True
    else:
        print("Incorrect!")
        return False


def math_roulette_challenge():
    list=[]
    op=["+","-","*"]
    for i in range(5):
        list.append(random.randint(1,20))
    o=random.choice(op)
    print(list)
    if o=="+":
        print("Compute the sum of the terms of this list")
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
        return True
    else:
        print("You lose !")
        return False

def solve_linear_equation():
    a,b=random.randint(1,10),random.randint(1,10)
    r=f"{-b}/{a}"
    z=str(int(-b/a))
    return a,b,r,z

def maths_solve_equation():
    a,b,r,z=solve_linear_equation()
    print("Solve the following equation:",a,"x +",b,"= 0")
    t=input("Enter your answer: ")
    if t==r or t==z:
        print("Correct! You win a key")
        return True
    else:
        print("Incorrect!")
        return False

def math_challenge():
    challenges= [math_challenge_factorial, math_roulette_challenge, maths_solve_equation]
    challenge= random.choice(challenges)
    print(challenge())

