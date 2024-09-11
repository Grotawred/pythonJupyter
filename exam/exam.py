add = lambda a, b: a + b
sub = lambda a, b: a - b
mult = lambda a, b: a * b
div = lambda a, b: a / b

def stringCalc(expression):
    res = 0
    expression = expression.replace(" ", "")
    try:
        for op in operations:
            if op in expression:
                expression = expression.split(op)
                a = float(expression[0])
                b = float(expression[1])
                res = operations[op](a, b)
                return res
    except Exception:
        return "Error, try one more"

operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
}

while True:
    a = input()
    if a == "exit":
        break
    res = stringCalc(a)

    with open('main.log', 'a') as file:
        file.write(a + " = " + str(res) + "\n")

    print(res)
