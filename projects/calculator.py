"""Mini Projects — calculator.py

Part of Python Beginner Guide: https://github.com/MehvishKiani/Python-beginner-guide
"""
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Enter 'q' to quit.")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                print(f"Result: {num1 / num2}")


if __name__ == "__main__":
    calculator()
