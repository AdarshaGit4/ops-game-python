import random
'''
1 for Rock
-1 for Paper
0 for Scissors
'''
computer = random.choice([-1, 0, 1])
print("Rock->r , Paper->p , Scissors->s")
youstr = input("Enter your choice: ")
youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}

you = youDict[youstr]

# Now we have 2 numbers (variables), you and computer.

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): 
        print("Sorry, You Lose!")

    elif(computer ==-1 and you == 0):
        print("Hurray,You Win!")

    elif(computer == 1 and you == -1):
        print("Hurray,You Win!")

    elif(computer ==1 and you == 0):
        print("Sorry, You Lose!")

    elif(computer ==0 and you == -1):
        print("Sorry, You Lose!")

    elif(computer == 0 and you == 1):
        print("Hurray,You Win!")

    else:
        print("Something went wrong!")