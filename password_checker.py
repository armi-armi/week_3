MIN_LENGTH = 5
MAX_LENGTH = 15
REQUIRES_SPECIAL_CHAR = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if REQUIRES_SPECIAL_CHAR:
        print(f"\tand 1 or more special characters:  {SPECIAL_CHARACTERS}")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")

def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = count_upper = count_digit = count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if REQUIRES_SPECIAL_CHAR and count_special == 0:
        return False

    return True

if __name__ == "__main__":
    main()