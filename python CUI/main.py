import calculator

def main():
    print("Welcome to the calculator")
    try:
        a = float(input("Enter the first number:\n"))
        op = input("Choose operation (+, -, *, /, **, %, sqrt): ")

        if op != "sqrt":
            b = float(input("Enter the second number:\n"))

        if op == "+":
            print("Result:", calculator.add(a, b))
        elif op == "-":
            print("Result:", calculator.substract(a, b))
        elif op == "*":
            print("Result:", calculator.multiply(a, b))
        elif op == "/":
            print("Result:", calculator.divide(a, b))
        elif op == "**":
            print("Result:", calculator.power(a, b))
        elif op == "%":
            print("Result:", calculator.modulus(a, b))
        elif op == "sqrt":
            print("Result:", calculator.square_root(a))
        else:
            print("Invalid operation.")

    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
