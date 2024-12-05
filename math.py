from random import *
f=0
def math_challenge_factorial():
    n=randint(1,10)
    print("Math challenge: Compute the factorial of ",n)
    k=1
    for i in range(1,n+1):
        k=k*i
    z=int(input("Enter your answer: "))
    if z==k:
        print("Correct! You win a key.")
    else:
        print("Incorrect!")

def linear_solve():
    a,b=randint(1,10),randint(1,10)
    print("Solve the following equation:",a,"x +",b)
    r=-b/a
    t=float(input("Enter your answer: "))
    if t==r:
        print("Correct! You win a key")
    else:
        print("Incorrect!")