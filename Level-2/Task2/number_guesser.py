# Create a number guessing game where the program generates a random number between a specified range, and the user tries to guess it. Provide feedback to the user if their guess is too high or too low.
import random

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))

secret_number = random.randint(low, high)
attempts = 0

print(f"Guess the number between {low} and {high}!")

# Loop until the user guesses the correct number
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1  # Increment the attempt count

    # Check if the guess is correct, too high, or too low
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
        break 