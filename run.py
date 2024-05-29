import random
import re
from os import system, name
from ascii_art import hangman_title, trophy, thanks, lets_go
import gallows

from music import bands
from cars import car_brands
from animals import animal_list


def title():
    """
    Generates the title screen for the game.
    """
    clear_screen()
    hangman_title()
    input()
    clear_screen()

def get_user_category():
    """
    Select a category to import specific words into the game
    """
    print("\nPlease choose one of the following categories:\n")
    print("     --- MUSIC --- CARS --- ANIMALS ---\n")
    user_category_choice = input("")
    clear_screen()

    print(f"\nYou chose {user_category_choice}\n")

    if user_category_choice == "music":
        return bands, "music"
    elif user_category_choice == "cars":
        return car_brands, "cars"
    elif user_category_choice == "animals":
        return animal_list, "animals"
    else:
        print(f"This is not a valid option! Please try again:")
    return get_user_category()

def random_word(secret_word):
    """
    Generate random word from imported list
    """
    # Assisted through information on Stack Overflow
    return random.choice(secret_word).upper()

def validate_guess(user_guess):
    """
    Validates the user's guess by checking it only contains letters or spaces.
    """
    try:
        if not all(entry.isalpha() or entry.isspace() for entry in user_guess):
            raise ValueError
    except ValueError:
        print("\nEntry not recognised. Please enter either a letter or space")
        user_guess
    else:
        return True

def user_guess():
    """
    This function prompts the user to guess a letter and then sends the user
    input to the validate_guess function.
    """
    while True:
        user_guess = input("\nPlease guess a letter: ").upper()
        if validate_guess(user_guess):
            return user_guess

def play_game():
    """
    Main game function
    """
    secret_word, category_name = get_user_category()
    answer = random_word(secret_word)
    clear_screen()
    print("You have 5 lives to work out the secret word.")
    print(f"The secret word is from your chosen catagory '{category_name.upper()}'")
    print("Good luck!\n")

    lives = 6
    guesses = []
    # How to avoid spaces courtesy of Stack Overflow
    hidden_answer = re.sub(r"\S", "_", answer)

    while lives > 0:
        """
        While loop runs until lives hit zero, player wins or
        enters "quit" to return to main menu
        """
        print(gallows.hanging_man[lives])
        print(f"Lives remaining: {lives}")
        print(f"Previous guesses: {guesses}\n")
        print(hidden_answer)

        guess = user_guess()
        
        if guess in guesses:
            clear_screen()
            print(f"\nNo no no! You have already tried '{guess}', try again!\n")
        elif guess == "QUIT":
            break
        elif len(guess) > 1:
            clear_screen()
            # Check to see if player has guessed a word
            print(f"You have guessed the word {guess}")
            # See if word is the correct answer
            if guess == answer:
                clear_screen()
                trophy()
                print(f"\nWell done, you win! The secret word was '{answer}'!")
                print(f"You beat the hangman and live to play another day!\n")
                play_again()
            else:
                lives -= 2
                clear_screen()
                print(f"\nNice try! But, '{guess}' is not the secret word!\n")
        elif guess in answer:
            hidden_answer = update_hidden_answer(hidden_answer, answer, guess)
            # Check to see if player has won
            if hidden_answer == answer:
                print(f"\n{hidden_answer}")
                break
            else:
                clear_screen()
                print(f"\nWell done! '{guess}' is in the secret word!\n")
        else:
            lives -= 1
            clear_screen()
            print(f"\nToo bad, '{guess}' is not in the secret word!\n")
        guesses.append(guess)
       
    if hidden_answer == answer:
        clear_screen()
        trophy()
        print(f"\nWell done! The secret word was '{answer}'!")
        print(f"You beat the hangman and live to play another day!\n")
        
    else:
        clear_screen()
        print(f"\n\nUh oh! You lose!\n")
        print(gallows.hanging_man[lives])
        print(f"The secret word was '{answer}', who knew?!\n")

    play_again()

def play_again():
    """
    Ask player if they want to play again
    """
    again = input("would you like to play again? (Y/N) ").upper()
        
    if again == "Y":
        clear_screen()
        lets_go()
        play_game()
    elif again == "N":
        clear_screen()
        thanks()
        input()
        title()
    else:
        print("Please enter either 'Y' or 'N'")
        play_again()

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

def clear_screen():
    """
    Clears the terminal
    """
    # learnt from https://www.geeksforgeeks.org/clear-screen-python/
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")

def main():
    """
    Main game function
    """
    title()
    play_game()

main()