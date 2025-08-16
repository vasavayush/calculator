class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def percentage(self, part, whole):
        if whole == 0:
            raise ValueError("Cannot calculate percentage with whole as zero")
        return (part / whole) * 100

# Example usage:

def main():
    calc = Calculator()
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Percentage")
        print("6. Exit")
        choice = input("Enter choice (1/2/3/4/5/6): ")
        if choice == '6':
            print("Exiting calculator.")
            break
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            continue
        try:
            if choice == '5':
                part = float(input("Enter the part value: "))
                whole = float(input("Enter the whole value: "))
                try:
                    print(f"Result: {calc.percentage(part, whole)}%")
                except ValueError as e:
                    print(e)
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"Result: {calc.add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {calc.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {calc.multiply(num1, num2)}")
                elif choice == '4':
                    try:
                        print(f"Result: {calc.divide(num1, num2)}")
                    except ValueError as e:
                        print(e)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
