# tools.py

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
            return "Invalid calculation format"

        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])

        return operators[op](num1, num2)

    except Exception as e:
        return str(e)