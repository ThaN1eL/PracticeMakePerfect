def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        # Get the users choice
        choice = input("Please enter the number of the operation you do like to perform (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                # Get the numbers to perform the operation on
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"The result of {num1} + {num2} is {num1 + num2}")
                elif choice == '2':
                    print(f"The result of {num1} - {num2} is {num1 - num2}")
                elif choice == '3':
                    print(f"The result of {num1} * {num2} is {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result of {num1} / {num2} is {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Error: Please enter valid numbers.")
        else:
            print("Invalid input. Please select a valid operation.")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Goodbye!")
            break

# Run the calculator
calculator()
