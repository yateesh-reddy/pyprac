def file_info():
    with open("file1.txt", "r") as f:
        data = f.read()

    print("Words:", len(data.split()))
    print("Vowels:", sum(c.lower() in "aeiou" for c in data))
    print("Spaces:", data.count(" "))
    print("Lowercase:", sum(c.islower() for c in data))
    print("Uppercase:", sum(c.isupper() for c in data))

file_info()