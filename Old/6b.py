with open("sample.txt", "r") as f:
    words = f.read().split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

word = max(freq, key=freq.get)

print("Most frequent word:", word)
print("Count:", freq[word])