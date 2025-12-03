def display_first_n_lines(file_name, n):
        with open(file_name, 'r') as file:
            for i in range(n):
                line = file.readline()
                if line:
                    print(line.strip())
                else:
                    break

def count_word_frequency(file_name, word):
    count = 0
    with open(file_name, 'r') as file:
            for line in file:
                count += line.lower().split().count(word.lower())

    return count

file_name = input("Enter the file name: ")
n = int(input("Enter the number of lines to display: "))
word = input("Enter the word to find its frequency: ")
print(f"\nFirst {n} lines of the file:")
display_first_n_lines(file_name, n)
word_count = count_word_frequency(file_name, word)
print(f"\nThe word '{word}' occurs {word_count} times in the file.")
