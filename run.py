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

word = random_word()
lives = 10

"""
Main game function
"""
def play_game():
    print(word)

    answer = word
    hidden_answer = "_ " * len(answer)
    print(hidden_answer)







welcome()
play_game()