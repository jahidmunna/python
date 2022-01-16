import re

PHONE_PATTERN = r"^(\+88)?01(7|8|5|)\d{8}$"

while True:
    user_input =str(input("Enter Phone: "))
    if user_input in ('q','Q'):
        break
    is_Valid = "Valid" if re.search(PHONE_PATTERN, user_input) else "Not Valid"

    print("[", user_input, "]\t", is_Valid)
