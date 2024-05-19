import random
from music import bands

catagories = ["music","cars", "general", "code", "institute"]
    
def random_word():
    """
    Generate random word from list
    """
    # Assisted through information on Stack Overflow
    return random.choice(bands).upper()

answer = random_word()

# def validate_guess():
#         try:
#             if len(guess) == 1 and guess.isalpha():
#                 raise ValueError(f"A single letter answer is required, you entered {len(guess)}")
#         except ValueError:
#             print("Please enter a single letter")
#             return False

def play_game():
    """
    Main game function
    """
    print("You have 5 lives to work out the secret word.")
    print("Good luck!\n")
    print(answer)

    lives = 5
    guesses = []
    hidden_answer = "_" * len(answer)

    while lives > 0:
        """
        While loop runs until lives hit zero, player wins or
        enters "quit" to return to main menu
        """
        print(f"Lives remaining: {lives}")
        print(f"Letters guessed: {guesses}\n")
        print(hidden_answer)

        guess = input("\nPlease guess a letter: ").upper()
        # validate_guess()
        if guess in guesses:
            print(f"\nNo no no! You have already tried '{guess}', try again!\n")
        elif guess == "QUIT":
            break
        # elif guess == answer:
        #     hidden_answer = update_hidden_answer(hidden_answer, answer, guess)
        #     guesses.append(guess)
        #     print(hidden_answer)
        #     break
        elif guess in answer:
            hidden_answer = update_hidden_answer(hidden_answer, answer, guess)
            guesses.append(guess)
            # Check to see if player has won
            if hidden_answer == answer:
                print(f"\n{hidden_answer}")
                break
            else:
                print(f"\nWell done! '{guess}' is in the secret word!\n")   
        else:
            lives -= 1
            print(f"\nToo bad, '{guess}' is not in the secret word!\n")
            guesses.append(guess)
       
    if hidden_answer == answer:
        print(f"\nWell done! The secret word was '{answer}'!")
        print(f"You beat the hangman and live to play another day!\n")
        
    else:
        print(f"\nUh oh! You lose!\n")
        print(f"The secret word was '{answer}', who knew?!\n")

    play_again()          

def play_again():
    try:
        again = input("would you like to play again? (Y/N) ").upper()
        again != "Y" or "N"
        if again == "Y":
            print(f"\n\nLETS GO ROUND AGAIN!\n\n")
            play_game()
        else:
            print(f"\n\nBye! See you again soon!\n\n")
            main()
    except ValueError():
        print("Please enter either 'Y' or 'N'")

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

def main():
    print("Welcome to HANGMAN!")
    print("Press any key to continue")
    input()
    play_game()

main()