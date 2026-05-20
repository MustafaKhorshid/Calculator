def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Convert Decimal to Binary & Hex")  
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '6':
        print("Exiting calculator. Goodbye!")
        break
        
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
            
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

    
    elif choice == '5':
        try:
            dec_num = int(input("Enter a whole decimal number to convert: "))
        except ValueError:
            print("Invalid input. Base conversion requires a whole number (integer).")
            continue
        

        binary_result = bin(dec_num)[2:]
        hex_result = hex(dec_num)[2:].upper()         
        print(f"\n--- Base Conversions for {dec_num} ---")
        print(f"Binary (Base 2):      {binary_result}")
        print(f"Hexadecimal (Base 16): {hex_result}")
            
    else:
        print("Invalid Choice. Please select a valid option from 1 to 6.")