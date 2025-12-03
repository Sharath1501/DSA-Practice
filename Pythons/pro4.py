from collections import Counter

def display_first_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines[:n]:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

def count_word_frequency(file_name, word):
    try:
        with open(file_name, 'r') as file:
            text = file.read().lower()  # Read the entire file and convert to lowercase
            words = text.split()  # Split text into words
            frequency = Counter(words)  # Count frequency of each word
            return frequency[word.lower()]  # Return the frequency of the specific word
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        return 0

file_name = input("Enter the file name: ")
n = int(input("Enter the number of lines to display: "))
word = input("Enter the word to find its frequency: ")
print(f"\nFirst {n} lines of the file:")
display_first_n_lines(file_name, n)
word_count = count_word_frequency(file_name, word)
print(f"\nThe word '{word}' occurs {word_count} times in the file.")
