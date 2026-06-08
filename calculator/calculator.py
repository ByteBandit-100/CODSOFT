import os
def calulate(a, b, ch):
    match ch:
        case 1: print(f"The Addition of {a:g} + {b:g} is {(a+b):g}")
        case 2: print(f"The Subtraction of {a:g} - {b:g} is {(a-b):g}")
        case 3: print(f"The Multiplication of {a:g} * {b:g} is {(a*b):g}")
        case 4:
                    if b == 0:
                        print("Division by zero is not allowed.")
                    else:
                        print(f"The Division of {a:g} / {b:g} is {(a/b):g}")

if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\r---------------- MENU ----------------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice.")

        if choice == 5:
            print("Thank you for using Calculator!")
            break

        try:
            if choice in [1, 2, 3, 4]:
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                calulate(a, b, choice)
        except ValueError:
            print("Please enter valid numbers.")
            input("\nPress Enter to continue...")
            continue
        input("\nPress Enter to continue...")