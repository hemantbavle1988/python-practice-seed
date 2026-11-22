
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

a = input1
b = input2

def add(a, b):
    result = a + b
    return result

def sub(a, b):
    if(a > b):
        result = a-b
    elif(a < b):
        result = b - a
    else:
        result = a - b
    return result

def mul(a, b):
    result = a*b
    return result

def div(a, b):
    if(b != 0):
        result = a/b
    else:
        result = "Division by zero is not allowed."
    return result


print(f"Addition of {a} and {b} is: {add(a, b)}")
print(f"Subtraction of {a} and {b} is: {sub(a, b)}")
print(f"Multiplication of {a} and {b} is: {mul(a, b)}")
print(f"Division of {a} and {b} is: {div(a, b)}")