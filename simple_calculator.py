def simple_calculator():
    print("Welcome to the Simple Calculator!")

    # Input two numbers from the user
    try:
        # Predefined input for environments that do not support interactive input
        inputs = [(5.0, 3.0), (10.0, 0.0), (7.0, 2.0)]  # Example test cases
        for num1, num2 in inputs:
            print(f"\nUsing predefined numbers: {num1} and {num2}")

            # Display operation choices
            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            # Input operation choice
            for choice in ['1', '2', '3', '4']:
                print(f"\nPerforming operation {choice}...")

                # Perform the chosen operation
                if choice == '1':
                    result = num1 + num2
                    print(f"The result of addition is: {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"The result of subtraction is: {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"The result of multiplication is: {result}")
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"The result of division is: {result}")
                    else:
                        print("Error! Division by zero is not allowed.")
                else:
                    print("Invalid choice! Please select a valid operation.")
    except ValueError:
        print("Invalid input! Please ensure all values are numeric.")

# Run the calculator program
simple_calculator()
