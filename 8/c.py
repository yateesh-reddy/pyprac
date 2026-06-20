ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
elif ch.islower():
    print("Lowercase")
elif ch.isupper():
    print("Uppercase")
else:
    print("Special Character")