import random
from words import words
import string
from hangman_visual import lives_visual_dict


def get_valid_word(words):
    word_guess = random.choice(words)
    if ("-" in word_guess or " " in word_guess):
        word_guess = random.choice(words)
    return word_guess.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 7
   
    while len(word_letters) > 0:
        print("You have used these letters ", " ".join(used_letter))

        current_word_letters = [letter if letter in used_letter else "_" for letter in word]
        print("Current word is ", " ".join(current_word_letters))

        user_ip_letter = input("Guess a letter. ").upper()
        if user_ip_letter in alphabet - used_letter:
            used_letter.add(user_ip_letter)

            if user_ip_letter in word:
                print("Yay! You guessed it correct.")
                word_letters.remove(user_ip_letter)
                continue
            else:
                print(f"The letter that you guessed {user_ip_letter} is not in the word. Please try again.")
                lives-=1
                print(f"You only have {lives} lives left. Chose wisely.")
                print(lives_visual_dict[lives])
                if lives == 0:
                    print("Ouch! You are out of lives. You lost!")
                    print(f"The word is {word}")
                    break
        elif user_ip_letter in used_letter:
            print(f"You have already guessed {user_ip_letter} perviously, Please try again. ")
            lives-=1
            print(f"You only have {lives} lives left. Chose wisely.")
            print(lives_visual_dict[lives])
            if lives == 0:
                print("Ouch! You are out of lives. You lost!")
                print(f"The word is {word}")
                break
        else:
            print("Invalid character. Please try again.")

    if lives != 0:
        print("Yay! You got the word!")


hangman()
