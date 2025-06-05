def calculate(expression):
    tokens = expression.split()

    # First, handle multiplication and division
    i = 1
    while i < len(tokens) - 1:
        if tokens[i] == '*':
            tokens[i-1] = float(tokens[i-1]) * float(tokens[i+1])
            del tokens[i:i+2]
            i -= 1  # Decrement i to account for the deleted elements
        elif tokens[i] == '/':
            tokens[i-1] = float(tokens[i-1]) / float(tokens[i+1])
            del tokens[i:i+2]
            i -= 1  # Decrement i to account for the deleted elements
        else:
            i += 2

    # Now, handle addition and subtraction
    result = float(tokens[0])
    i = 1
    while i < len(tokens) - 1:
        operator = tokens[i]
        operand = float(tokens[i+1])
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        i += 2

    return result

if __name__ == "__main__":
    expression = "3 + 7 * 2"
    print(calculate(expression))
