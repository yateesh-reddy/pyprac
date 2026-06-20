def find_word(filename, word):
    with open(filename, "r") as f:
        data = f.read()

    if word in data:
        print("Word found")
    else:
        print("Word not found")

find_word("sample.txt", "python")