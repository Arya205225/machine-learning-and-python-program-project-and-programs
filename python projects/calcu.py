history_file = "history.txt"

def show_history():
    try:
        with open(history_file, "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history found")

def clear_history():
    open(history_file, "w").close()
    print("History cleared")

def save_history(equation, result):
    with open(history_file, "a") as file:
        file.write(equation+" = "+str(result)+"\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in format: number operator number (e.g., 5 + 2)")
        return

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Division by zero is not allowed")
            return
        result = num1 / num2
    elif operator == "%":
        if num2 == 0:
            print("Division by zero is not allowed")
            return
        result = num1 % num2
    else:
        print("Invalid operator. Use one of: +, -, *, /, %")
        return

    if isinstance(result, float) and result.is_integer():
        result = int(result)
    print("Result:", result)
    save_history(user_input, result)

def main():
    while True:
        user_input = input("Enter equation (e.g., 5 + 2) or 'history', 'clear', 'exit': ").strip()
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()