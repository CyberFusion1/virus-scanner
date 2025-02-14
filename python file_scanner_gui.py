
                                                                   python                                                                                  
# Simple Calculator script

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Displaying options for the user
def display_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main function for the calculator
def calculator():
    while True:
        display_menu()
# Taking user input for operation choice
        choice = input("Enter choice (1/2/3/4/5): ")

        # If user chooses to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Checking if the user input is a valid operation
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Performing the operation based on the user's choice
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid operation.")

 # Asking the user if they want to perform another calculation
        continue_calc = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if continue_calc != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Run the calculator function
if __name__ == "__main__":
    calculator()

# Navigate to your project folder
cd path/to/your-virus-scanner

# Initialize a Git repository
git init

# Link it to your GitHub repository
git remote add origin https://github
