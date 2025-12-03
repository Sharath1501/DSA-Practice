def countin():
    filename = input("Enter the name of text file : ")
    num_lines = int(input("Enter the number of lines to be displayed:"))
    word = input("Enter the word ot be displayed:").lower()

    with open(filename,'r') as file:
        for _ in range(num_lines):
            line = file.readline()
            if not line:
                break
            print(line.strip())
        word_count = sum(line.lower().strip().count(word) for line in file)

        print(f"the word {word} appears {word_count} in the file")
countin()
            