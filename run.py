import random


words = ["test","python", "computer", "code", "institute"]

def welcome():
    print("Welcome to HANGMAN!")
    print("You have 10 guesses to work out the secret word.")
    print("Good luck!")

"""
Generate random word from list
"""
def random_word():
    return random.choice(words)

answer = random_word()

"""
Main game function
"""
def play_game():
    print(answer)

    lives = 10
    hidden_answer = "_ " * len(answer)
    print(hidden_answer)

    while lives > 0:
        print(lives)

        guess = input("Please guess a letter: ")
        if guess in answer:
            print(f"Well done! {guess} is in the secret word!\n")
        elif guess == "quit":
            break
        else:
            lives -= 1
            print(f"Too bad, {guess} is not in the secret word!\n")



welcome()
play_game()