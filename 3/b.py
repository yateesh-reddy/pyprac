import re

phone = input("Enter phone number: ")
email = input("Enter email: ")

if re.fullmatch(r"\d{10}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
    print("Valid email")
else:
    print("Invalid email")