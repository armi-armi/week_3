# Write name to a file
name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

# Read name from the file and print
with open("name.txt", 'r') as file:
    name = file.read().strip()
print(f"Hi {name}!")

# Read first two numbers and add them
with open("numbers.txt", 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
print(number1 + number2)

# Calculate total of all numbers in the file
with open("numbers.txt", 'r') as file:
    total = sum(int(line) for line in file)
print(total)