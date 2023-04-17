import random

def guess(x):
    guess = 0
    random_number = random.randint(1,x)
    while(guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if (guess > random_number):
            print("Too high")
        elif(guess < random_number):
            print("Too low")
    return guess

ans = guess(10)
print(f"yay you won the answer is {ans}")
