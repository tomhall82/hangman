import random


words = ["test","python", "computer", "code", "institute"]

def welcome():
    print("Welcome to HANGMAN!")
    print("You have 10 guesses to work out the secret word.")
    print("Good luck!\n")

"""
Generate random word from list
"""
def random_word():
    return random.choice(words)

answer = random_word()

def play_game():
    """
    Main game function
    """
    print(answer)

    lives = 5
    guesses = []
    hidden_answer = "_ " * len(answer)

    while lives > 0:
        """
        While loop runs until lives hit zero, player wins or
        enters "quit" to return to main menu
        """
        print(hidden_answer)
        print(f"Lives remaining: {lives}")
        print(f"Letters guessed: {guesses}")

        guess = input("Please guess a letter: ")
        if guess in answer:
            print(f"\nWell done! {guess} is in the secret word!\n")
            hidden_answer = update_hidden_answer(hidden_answer, answer, guess)
            guesses.append(guess)
        elif guess == "quit":
            break
        else:
            lives -= 1
            print(f"\nToo bad, {guess} is not in the secret word!\n")
            guesses.append(guess)

def update_hidden_answer(current_hidden_answer, answer, guess):
    """
    Update hidden answer to show correctly guessed letters
    """
    new_hidden_answer = ""
    for x in range(len(answer)):
        if answer[x] == guess:
            new_hidden_answer += guess
        else:
            new_hidden_answer += current_hidden_answer[x]
    return new_hidden_answer

welcome()
play_game()