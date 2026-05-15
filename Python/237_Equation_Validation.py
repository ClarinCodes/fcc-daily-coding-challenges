#04-04-2026 | 04-04-2026

'''
    Args: equation (str): Equation in the format "numbers and operators = number".
    Problem: Check if a simple arithmetic equation is correct.
    Returns: bool: True if the equation is correct, False otherwise.

    Note: Follows standard operator precedence (* and / before + and -).
'''


def is_valid_equation(equation):
    lhs, rhs = equation.split("=")
    lhs = lhs.strip()
    rhs = int(rhs.strip())

    # split and convert numbers
    tokens = lhs.split()
    expr = []
    for t in tokens:
        if t.isdigit():
            expr.append(int(t))
        else:
            expr.append(t)

    # handle * and / first
    new_expr = [expr[0]]  # start with first number
    i = 1
    while i < len(expr):
        op = expr[i]    # operator
        num = expr[i + 1]

        if op == '*':
            new_expr[-1] = new_expr[-1] * num
        elif op == '/':
            new_expr[-1] = new_expr[-1] // num  # integer division
        else:
            new_expr.append(op)
            new_expr.append(num)

        i += 2

    # handle + and -
    result = new_expr[0]
    i = 1
    while i < len(new_expr):
        op = new_expr[i]
        num = new_expr[i + 1]

        if op == '+':
            result += num
        else:
            result -= num
        i += 2

    return result == rhs

def test_cases():
    print(str(is_valid_equation("2 + 3 - 1 = 4")))       # "True"
    print(str(is_valid_equation("8 / 2 = 4")))           # "True"
    print(str(is_valid_equation("10 * 5 = 50")))         # "True"
    print(str(is_valid_equation("2 + 5 = 6")))           # "False"
    print(str(is_valid_equation("10 - 2 * 3 = 24")))     # "False"
    
if __name__ == "__main__":
    test_cases()
