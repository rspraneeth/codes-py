def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    num1 = float(input("What's the first number: "))
    for key in operations:
        print(key)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an operation symbol from above: ")
        num2 = float(input("What's the second number: "))
        op = operations[operation_symbol]
        answer = op(num1, num2)
        print(answer)
        rep = input("Type 'y' if you want to continue, 'n' if you want to exit, type 'new' if you want to start new "
                    "calculation: ")
        if rep == 'y':
            num1 = answer
        elif rep == 'new':
            calculator()
        else:
            should_continue = False


calculator()
