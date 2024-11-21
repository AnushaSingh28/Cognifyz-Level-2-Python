# Write a Python function that generates the Fibonacci sequence up to a given number of terms. The function should take an integer input from the user and display the Fibonacci sequence up to that number of terms.
def generate_fibonacci(n):
    # Starting values for the Fibonacci sequence
    num1, num2 = 0, 1
    
    # Print the Fibonacci sequence up to 'n' terms
    for _ in range(n):
        print(num1, end=" ")  # Display the current term
        num1, num2 = num2, num1 + num2  # Update the next two terms

# Ask the user for how many Fibonacci numbers they want
terms = int(input("How many terms do you want in the Fibonacci sequence? "))
generate_fibonacci(terms)
