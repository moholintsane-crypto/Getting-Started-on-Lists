# Function to calculate the square of a number from the user
def square_number():
    try:
        # Get user input and convert it to a float to handle decimals
        user_input = input("Enter a number to square: ")
        number = float(user_input) # Convert string input to a number
        
        # Calculate square using the exponentiation operator (**)
        result = number ** 2

        print(f"The square of {number} is {result}")
    except ValueError:
        print("Invalid error input! Please enter a valid numerical value.")

if __name__ == "__main__":
    square_number()