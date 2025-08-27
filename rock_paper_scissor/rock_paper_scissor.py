import random

def rps_game(x):
   
    winner = ""

    for i in range(0, x):
        user_input = input(f"Dear User, Please select one among ROCK, PAPER and SCISSOR \n")
        comp_input = random.choice(["ROCK", "PAPER", "SCISSOR"])
        print(f"user_input={user_input} and comp_input={comp_input}")
        if comp_input == user_input:
            print("user and computer choose the same option")
            continue
        elif user_input == "ROCK" and comp_input == "PAPER":
            winner = "Computer"
        elif user_input == "PAPER" and comp_input == "SCISSOR":
            winner = "Computer"
        elif user_input == "SCISSOR" and comp_input == "ROCK":
            winner = "Computer"
        else:
            winner = "User"
        print(f"Yay! Congrats, {winner} won this game \U0001F389")

print("***** Welcome to Rock Paper Scissor game *****")
print("\U0001f600")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("^_^ Lets Start The Game ^_^")

x = int(input("Dear User, Please enter the number of times you want you play the game, should be greater than 1 and less than 15"))
rps_game(x)
