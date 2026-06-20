with open("file.txt", "r") as f:
    words = f.read().split()

word = max(set(words), key=words.count)

print("Most frequent word:", word)
print("Count:", words.count(word))