input_number1 = int(input("Enter the first number: "))
input_number2 = int(input("Enter the second number: "))
input_number3 = int(input("Enter the third number: "))
input_operation = input("Enter the operation (+, -, *, /): ")

def sum_of_three_numbers(num1, num2, num3):
    result = num1 + num2 + num3
    return result

def division_of_three_numbers(num1, num2, num3):
    if(num1 != 0 and num2 != 0 and num3 != 0):
        result = num1 / num2 / num3
    elif(num1 == 0 or num2 == 0 or num3 == 0):
        result = "Division by zero is not allowed."
    else:
        result = "Invalid operation."
    return result

def multiplication_of_three_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

def subtraction_of_three_numbers(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        result = num1 - num2 - num3
    elif(num2 > num1 and num2 > num3):
        result = num2 - num1 - num3
    elif(num3 > num1 and num3 > num2):
        result = num3 - num1 - num2
    elif(num1 == num2 and num1 == num3):
        result = num1 - num2 - num3 
    return result

def perform_operation(num1, num2, num3, op):
    if op == "+":
        return sum_of_three_numbers(num1, num2, num3)
    elif op == "-":
        return subtraction_of_three_numbers(num1, num2, num3)
    elif op == "*":
        return multiplication_of_three_numbers(num1, num2, num3)
    elif op == "/":
        return division_of_three_numbers(num1, num2, num3)
    else:
        return "Invalid operation."

final_result = perform_operation(input_number1, input_number2, input_number3, input_operation)
print(f"The result of {input_number1} {input_operation} {input_number2} {input_operation} {input_number3} is: {final_result}")  

