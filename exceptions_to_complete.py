is_valid_input = False
while not is_valid_input:
    try:
        result = int(input("Enter a number: "))
        is_valid_input = True
    except ValueError:
        print("Invalid input; enter a valid number.")
print(f"The valid number is {result}")