#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/9/2023
# This program allows the user to guess a number between 0 and 9.
# It uses a while TRUE loop to continue asking the user to guess the number, until they guess correctly.
# It uses a break statement to end the loop.

# Importing the random module.
import random


def main():
    # Initializing counter.
    counter = 0

    # Declaring a variable for the random number.
    random_number = random.randint(0, 9)

    # Initiating while loop.
    while True:
        # Explaining my program the th user.
        print(
            "My program will generate a random number between 0 and 9. Try to guess the correct number!"
        )

        # Getting user input.
        user_number_as_string = input("Please enter your guess: ")

        # Initiating try catch.
        try:
            # Converting user input from string to integer.
            user_number_as_int = int(user_number_as_string)

            # Using an if statement to check if the number guessed is in range of 0-9.
            if user_number_as_int >= 0 and user_number_as_int <= 9:
                counter = counter + 1

                # Using and if statement to see if the user guessed correctly.
                if user_number_as_int == random_number:
                    print(
                        "You guessed correctly! The number was {}.".format(
                            random_number
                        )
                    )
                    # Using break statement to exist the loop.
                    break

                # Else tell the user that their guess is wrong and display the amount of time the loop ran.
                else:
                    print("Your guessed wrong.Guess again!".format(random_number))
                    print("Tracking {} times through the loop.".format(counter))

            # Else tell the user that their number is not within the range.
            else:
                print(
                    "Your number is not within the range of 0 to 9. Please try again."
                )

        # Catching any errors.
        except:
            print("Invalid input.")


if __name__ == "__main__":
    main()
