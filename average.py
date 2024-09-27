# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Avoid division by zero
    return sum(numbers) / len(numbers)

# Main program
def main():
    numbers = []
    print("Enter numbers one by one (type 'done' when finished):")

    while True:
        user_input = input("Enter a number: ")

        # Check if the user is done entering numbers
        if user_input.lower() == 'done':
            break

        # Try to convert input to a float and add to the list
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a valid number or 'done'.")

    # Calculate and display the average
    average = calculate_average(numbers)
    print(f"The average of the entered numbers is: {average}")

# Run the program
if __name__ == "__main__":
    main()
