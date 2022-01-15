import re

EMAIL_PATTERN = r"[a-zA-Z]+[0-9]*@[a-zA-Z]+\.(com|edu|net)"

while True:
    user_input =str(input("Enter E-Mail: "))
    is_Valid = "Valid" if re.search(EMAIL_PATTERN, user_input) else "Not Valid"

    print("[", user_input, "]\t", is_Valid)
