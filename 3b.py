import re

phone = input("Enter phone number: ")
email = input("Enter email: ")

if re.fullmatch(r"\d{10}", phone):
    print("Valid Phone")
else:
    print("Invalid Phone")

if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
    print("Valid Email")
else:
    print("Invalid Email")