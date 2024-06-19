"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
def get_valid_number(prompt):
    """Ask the user for a valid integer and return it."""
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("That's not a valid number. Please enter a valid integer.")

def get_valid_guess(prompt, low, high):
    """Ask the user for a valid integer within the range and return it."""
    while True:
        try:
            guess = int(input(prompt))
            if low <= guess <= high:
                return guess
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("That's not a valid number. Please enter a valid integer.")

def advancedGuessingGame():
    """Play a guessing game with a user."""
    print("Welcome to the advanced guessing game!")
    
    # Get the lower bound
    low = get_valid_number("Enter the lower bound: ")
    
    # Get the upper bound
    while True:
        high = get_valid_number("Enter the upper bound: ")
        if high > low:
            break
        else:
            print(f"The upper bound must be greater than the lower bound ({low}). Please try again.")
    
    print(f"OK then, guess a number between {low} and {high}!")

    # Generate the random number to guess
    import random
    target = random.randint(low, high)
    
    while True:
        guess = get_valid_guess("Enter your guess: ", low, high)
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {target} correctly!")
            break

# Example usage:
advancedGuessingGame()


