try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# Answer: A ValueError will occur when the input is not a valid integer.

# When will a ZeroDivisionError occur?
# Answer: A ZeroDivisionError will occur when the denominator is zero.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Answer: Yes, by adding a check before performing the division.