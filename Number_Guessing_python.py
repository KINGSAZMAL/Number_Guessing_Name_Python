import random as r

def rand_num():
    a=int(input("Enter the starting range:"))
    b=int(input("Enter the ending range:"))
    return r.randint(a,b)

print("Welcome to number guessing game")
x=rand_num()
count=0
status=True
while(status):
    guess_number=int(input("Enter your number:"))
    count=count+1
    if(guess_number==x):
        print(x,"YOUR GUESS IS CORRECT")
        print("You took ",count,"times")
        dec=int(input("THANK YOU FOR PLAYING \n Do you want to play again \n 1.Yes  2.No  :"))
        if (dec!=1):
            status=False
        else:
            x=rand_num()
            count=0
    elif(guess_number>x):
        print("The number is lower than your guess")
    elif(guess_number<x):
        print("The number is greater than your guess")
    if(count>=5):
        b=int(input("Do you still wanna continue \n 1.yes 2.no  :"))
        if(b!=1):
            print("Thanks for Playing.")
            status=False
