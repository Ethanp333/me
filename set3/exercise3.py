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
import random

def get_valid_number(prompt):
    """Prompt the user for a valid integer, repeating until one is provided."""
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("That's not a valid number. Please enter a valid integer.")

def get_number_within_bounds(prompt, low, high):
    """Prompt the user for a number within bounds, repeating until one is provided."""
    while True:
        number = get_valid_number(prompt)
        if low <= number <= high:
            return number
        else:
            print(f"The number is outside the bounds. Please enter a number between {low} and {high}.")

def advancedGuessingGame():
    """Play a guessing game with the user, allowing custom bounds and handling invalid inputs."""
    print("\nWelcome to the advanced guessing game!")

    # Set the lower bound
    lower_bound = get_valid_number("Enter the lower bound: ")
    
    # Ensure the upper bound is greater than the lower bound
    while True:
        upper_bound = get_valid_number("Enter the upper bound: ")
        if upper_bound > lower_bound:
            break
        else:
            print("The upper bound must be greater than the lower bound. Please try again.")

    print(f"OK then, a number between {lower_bound} and {upper_bound}?")

    actual_number = random.randint(lower_bound, upper_bound)
    guessed = False

    while not guessed:
        guessed_number = get_number_within_bounds(f"Guess a number between {lower_bound} and {upper_bound}: ", lower_bound, upper_bound)
        print(f"You guessed {guessed_number},")
        if guessed_number == actual_number:
            print(f"You got it!! It was {actual_number}")
            guessed = True
        elif guessed_number < actual_number:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")

    return "You got it!"

if __name__ == "__main__":
    advancedGuessingGame()

# Example usage:
advancedGuessingGame()


