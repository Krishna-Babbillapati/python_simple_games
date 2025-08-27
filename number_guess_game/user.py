import random

def user_guess_game(x):
    comp_guess = random.randint(1, x)
    user_guess = int(input("Dear User, Please enter a random number between 1 and {}".format(x)))
    while user_guess != comp_guess:
        if user_guess > comp_guess:
            print("Hey User, Its too high")
            user_guess = int(input("Please enter a lower number, which should be greater than 1"))
        elif user_guess < comp_guess:
            print("Hey User, Its too low")
            user_guess = int(input("Please enter a higher number, which should be less than {}".format(x)))
        else:
            break
    return "Yay! You guessed it correct \U0001F389"

print("***** Welcome to Number Guess game *****")
print("\U0001f600")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("^_^ Lets Start The Game ^_^")

x = input("Dear User, Please enter a number which is max limit for this game")
print(user_guess_game(int(x)))

