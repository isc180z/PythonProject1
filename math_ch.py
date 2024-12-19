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
    factorial(n)
    z=int(input("Enter your answer: "))
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
        return True
    else:
        print("You lose !")
        return False


def solve_linear_equation():
    a,b=random.randint(1,10),random.randint(1,10)
    print("Solve the following equation:",a,"x +",b,"= 0")
    r=f"{-b}/{a}"
    z=str(int(-b/a))
    t=input("Enter your answer: ")
    if t==r or t==z:
        print("Correct! You win a key")
        return True
    else:
        print("Incorrect!")
        return False

def math_challenge():
    challenges= [math_challenge_factorial, math_roulette_challenge, solve_linear_equation]
    challenge= random.choice(challenges)
    print(challenge())
