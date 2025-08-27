import random

def comp_guess_game(x):
    low = 1
    high = x
    user_guess = int(input(f"Dear User, Please guess a number between 1 and {x}"))
    f = ""
    while f != "C":
        comp_guess = random.randint(low, high)
        f = str(input(f"Computer guess is {comp_guess}, Please enter 'C' if its correct, enter 'H' if its high or enter 'L' if its low"))
        if f == "L":
            low = comp_guess + 1
        elif f == "H":
            high = comp_guess - 1
    return f"Yay, compuer guessed the number {comp_guess} correct \U0001F389"


print("***** Welcome to Computer Number Guess game *****")
print("\U0001f600")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("^_^ Lets Start The Game ^_^")

print(comp_guess_game(100))
