# My cutesie calculator app
def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

def calculator():
    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. I want out")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Bye twin")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. PLEASE check the choices")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers...")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        print("Result:", result)

calculator()