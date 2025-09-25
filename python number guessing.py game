import random
print("first u need to select the range from which number to which number that you want to guess")
low=int(input("enter the lowest range you want to guess:"))
high=int(input("enter the highest range you want to guess:"))
number=random.randint(low,high)
while True:
    a=int(input(f"guess the number between {low} to {high}:" ))
    if number==a:
        print ("you won")
        sai=(input("you want to continue(y/n)"))
        if sai=="y":
             continue
        else:
           print("your quit from game")
           break
    elif number>a:
        print("greater")
    elif number<a:
        print("less")
    else:
        print ("you lose")
