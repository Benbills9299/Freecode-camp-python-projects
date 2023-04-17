#rock paper scissors
import random

def rockpapscissors(): #function that takes user input and random choice from computer
    user = input("Choose your choice P for Paper, S for scissors and R for rock:").lower()
    computer = random.choice(['r','p','s'])
    print(f"you choose {user}")
    print(f"computer choose {computer}")
    if user == computer:
        return "it is a tie"
    if win(user,computer):
        return "you won"
    else:
        return "you lost"
    
def win(a, b): #function to determine if a wins b using rock and paper rule
    if (a == 'p' and b == 'r') or (a == 'r' and b == 's') or (a == 's' and b == 'p'):
        return True
i = 0
user = 0 #holds result for user
computer = 0 #holds result for computer
while(i < 3): #will loop calling the rockpapscissors function three times as it is normally done in the game
    verdict = rockpapscissors()
    print(verdict)
    
    if verdict == "you won":
        user +=1
    elif verdict == "you lost":
        computer +=1
    i+=1
#if statements to determine final winner it checks if user score is higher than computer score
if user > computer:
    print("FINAL VERDICT: You won after three round")
elif computer > user:
    print("FINAL VERDICT: you lost after three round")
else:
    print("FINAL VERDICT: It is a tie after three round")
