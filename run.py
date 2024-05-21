import random
import re
import os
from ascii_art import hangman_title, trophy
import gallows

from music import bands
from cars import car_brands
from animals import animal_list


def title():
    clear_screen()
    hangman_title()
    print("\nPress enter to play!\n")
    input()
    clear_screen()

def get_user_catagory():
    """
    Select a catagory to import specific words into the game
    """
    print("Please choose one of the following catagories:\n")
    print("--- MUSIC --- CARS --- ANIMALS ---\n")
    user_catagory_choice = input("")
    clear_screen()
    # I want to move this out into the game option to show what catagory
    # the user is playing but can't get it to work?!
    print(f"\nYou chose {user_catagory_choice}")

    if user_catagory_choice == "music":
        return bands, "music"
    elif user_catagory_choice == "cars":
        return car_brands, "cars"
    elif user_catagory_choice == "animals":
        return animal_list, "animals"
    else:
        print(f"This is not a valid option! Please try again")
    return get_user_catagory()

def random_word(secret_word):
    """
    Generate random word from imported list
    """
    # Assisted through information on Stack Overflow
    return random.choice(secret_word).upper()

def validate_guess(user_guess):
    try:
        if user_guess.isalpha():
            return True
    except ValueError:
        print("Please enter a letter")
        return False

def user_guess():
    user_guess = input("\nPlease guess a letter: ").upper()
    if validate_guess(user_guess):
        return user_guess
    else:
        user_guess()

def play_game():
    """
    Main game function
    """
    secret_word, catagory_name = get_user_catagory()
    answer = random_word(secret_word)
    clear_screen()
    print("You have 5 lives to work out the secret word.")
    print(f"The secret word is from your chosen catagory '{catagory_name.upper()}'")
    print("Good luck!\n")
    print(answer)

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
        print(f"Letters guessed: {guesses}\n")
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
                print(f"\nWell done! The secret word was '{answer}'!")
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
    try:
        again = input("would you like to play again? (Y/N) ").upper()
        again != "Y" or "N"
        if again == "Y":
            clear_screen()
            print(f"\n\nLETS GO AGAIN!\n\n")
            play_game()
        else:
            clear_screen()
            print(f"\n\nBye! See you again soon!\n\n")
            print("Press enter to continue\n")
            input()
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

def clear_screen():
    """
    Clears the terminal
    """
    # learnt from https://www.geeksforgeeks.org/clear-screen-python/
    os.system("cls")

def main():
    title()
    play_game()

main()