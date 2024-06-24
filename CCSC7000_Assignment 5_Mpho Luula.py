# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:29:45 2024

@author: Mpho
"""

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def floor_divide(num1, num2):
    return num1 // num2

def modulus(num1, num2):
    return num1 % num2

def exponentiate(num1, num2):
    return num1 ** num2

def perform_operation(choice, num1, num2):
    if choice == "1":
        return add(num1, num2)
    elif choice == "2":
        return subtract(num1, num2)
    elif choice == "3":
        return multiply(num1, num2)
    elif choice == "4":
        return divide(num1, num2)
    elif choice == "5":
        return floor_divide(num1, num2)
    elif choice == "6":
        return modulus(num1, num2)
    elif choice == "7":
        return exponentiate(num1, num2)
    else:
        return None

def check_odd_even(result):
    if result % 2 == 0:
        return "Result is even"
    else:
        return "Result is odd"

def main():
    while True:
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Floor Divide")
        print("6. Modulus")
        print("7. Exponentiate")
        print("8. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == "8":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            num1, num2 = get_numbers()

            try:
                result = perform_operation(choice, num1, num2)
                print(f"Result: {result}")
                print(check_odd_even(result))
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    main()