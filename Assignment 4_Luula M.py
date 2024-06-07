# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:46:50 2024

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
 
def perform_operation(choice, num1, num2): 
    if choice == "1": 
        return num1 + num2 
    elif choice == "2": 
        return num1 - num2 
    elif choice == "3": 
        return num1 * num2 
    elif choice == "4": 
        return num1 / num2 
    elif choice == "5": 
        return num1 // num2 
    elif choice == "6": 
        return num1 % num2 
    elif choice == "7": 
        return num1 ** num2 
    else:
        return None

def check_odd_even(result): 
    if result % 2 == 0: 
        return "Result is even" 
    else: 
        return "Result is odd" 

while True: 
    print("Menu:") 
    print("1. Addition") 
    print("2. Subtraction") 
    print("3. Multiplication") 
    print("4. Normal Division") 
    print("5. Floor Division") 
    print("6. Modulus") 
    print("7. Exponentiation") 

    choice = input("Enter your choice (1-7): ") 

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice. Please enter a number between 1 and 7.")
        continue

    num1, num2 = get_numbers() 
    result = perform_operation(choice, num1, num2)

    if result is not None:
        odd_even = check_odd_even(result) 
        print(f"You entered: {num1} and {num2}") 
        print(f"Result: {result}") 
        print(odd_even) 
    else:
        print("An error occurred with the operation.")

    repeat = input("Do you want to perform another operation? (yes/no): ") 
    if repeat.lower() != "yes": 
        print("Goodbye!") 
        break