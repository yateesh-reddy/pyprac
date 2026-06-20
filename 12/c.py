import re

phone = input("Phone: ")
email = input("Email: ")

print("Valid Phone" if re.fullmatch(r"\d{10}", phone) else "Invalid Phone")
print("Valid Email" if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email) else "Invalid Email")