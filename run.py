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

    lives = 5
    guesses = []
    hidden_answer = "_ " * len(answer)
    print(hidden_answer)

    while lives > 0:
        print(f"Lives remaining: {lives}")
        print(f"Letters guessed: {guesses}")

        guess = input("Please guess a letter: ")
        if guess in answer:
            print(f"\nWell done! {guess} is in the secret word!\n")
            guesses.append(guess)
        elif guess == "quit":
            break
        else:
            lives -= 1
            print(f"\nToo bad, {guess} is not in the secret word!\n")
            guesses.append(guess)



welcome()
play_game()