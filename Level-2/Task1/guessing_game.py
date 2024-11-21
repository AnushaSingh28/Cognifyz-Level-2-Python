# Write a Python program that generates a random number between 1 and 100. The user should then try to guess the number. The program should provide hints such as "too high" or "too low" until the correct number is guessed.
import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts = attempts + 1  
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break  

guess_number()
