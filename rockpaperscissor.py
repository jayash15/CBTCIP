import random
choices = ["rock","paper","scissors"]

yourchoice = input("choose rock , paper or scissors")

devicechoice = random.choice(choices)

print("you choose", yourchoice)

print("device choose",devicechoice)

if yourchoice == devicechoice:

    print("It's a tie")

elif yourchoice == "rock" and devicechoice == "scissors":

    print("You win")

elif yourchoice == "paper" and devicechoice == "rock":

    print("You win")

elif yourchoice == "scissors" and devicechoice == "paper":

    print("You win")

else:

    print("device wins")

