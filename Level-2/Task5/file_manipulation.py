# Write a Python program that reads a text file and counts the occurrences of each word in the file. Display the results in alphabetical order along with their respective counts.
def count_words_in_file(filename):
    # Open the file and read the contents
    try:
        with open(filename, 'r') as file:
            text = file.read()
        
        # Convert text to lowercase and split into words
        words = text.lower().split()

        # Create a dictionary to store word counts
        word_count = {}
        
        # Count the occurrences of each word
        for word in words:
            word = word.strip('.,!?";:')  # Remove punctuation marks from each word
            if word:  # Check if word is not empty
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        # Print the word counts in alphabetical order
        for word in sorted(word_count):
            print(word, ":", word_count[word])

    except FileNotFoundError:
        print("Error: The file", filename, "was not found.")


filename = input("Enter the name of the text file: ")
count_words_in_file(filename)
