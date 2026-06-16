import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculator_tool(expression):
    try:
        parts = expression.split()

        if len(parts) != 3:
            return "Invalid format. Use: number operator number"

        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])

        if op not in operators:
            return "Unsupported operator"

        result = operators[op](num1, num2)
        return result

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_input = input("Enter calculation: ")
    print("Result:", calculator_tool(user_input))