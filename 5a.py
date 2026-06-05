with open("file1.txt", "r") as f:
    text = f.read()

words = len(text.split())
vowels = sum(ch.lower() in "aeiou" for ch in text)
spaces = text.count(" ")
lower = sum(ch.islower() for ch in text)
upper = sum(ch.isupper() for ch in text)

print("Words:", words)
print("Vowels:", vowels)
print("Spaces:", spaces)
print("Lowercase:", lower)
print("Uppercase:", upper)