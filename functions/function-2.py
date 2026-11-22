input_number1 = int(input("Enter the first number: "))
input_number2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")


def perform_operation(num1, num2, op):
    if op == "+":
       return add(num1, num2)
    elif op == "-":
        return sub(num1, num2)
    elif op == "*":
        return mul(num1, num2)
    elif op == "/":
        return div(num1, num2)
    else:
        return "Invalid operation."


def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    if(num1 > num2):
        result = num1 - num2
    else:
        result = num2 - num1
    return result

def mul(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    if(num2 != 0):
        result = num1 / num2
    else:
        result = "Division by zero is not allowed."
    return result


final_result = perform_operation(input_number1, input_number2, operation)
print(f"The result of {input_number1} {operation} {input_number2} is: {final_result}")