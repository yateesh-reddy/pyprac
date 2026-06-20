def find_word(file, word):
    with open(file, "r") as f:
        text = f.read()

    if word in text:
        print("Word Found")
    else:
        print("Word Not Found")

find_word("sample.txt", input("Enter word: "))