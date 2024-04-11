def is_armstrong(number):
    # Convert the number to a string to count the digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the Armstrong sum
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the number is an Armstrong number
    return armstrong_sum == number

# Take input from the user
user_input = input("Enter a number: ")

try:
    # Convert user input to an integer
    number = int(user_input)
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
