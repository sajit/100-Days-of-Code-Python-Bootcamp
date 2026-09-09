def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

ops = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operation = input("Enter operation: ")
print(ops[operation](n1, n2))
