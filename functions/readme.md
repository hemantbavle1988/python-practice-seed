## FUNCTIONS IN PYTHON ##


# Functions are reusable blocks of code that should perform a specific tasks.

# They are essential for organizing your code, making it more modular
# and easier to maintain.

"""
1. declaration -> telling interpretor that this is the name of the code
i want to reuse.

2. defination -> I will write the actual code to do something

3. function call -> we use function name where ever we want to reuse the code.
  
"""


# 1. Declaring a Function :

# def keyword: This keyword marks the beginning of a function Declaration.

# Function Name: Choose a descriptive name that reflects the function's purpose
# (e.g., calculate_area, greet, etc.).

# Parameters (Optional): Parameters act like variables within the function
# body, allowing you to pass data (arguments) when calling the function.

# They are enclosed within parentheses () in function declaration.

# Colon (:): A colon indicates the start of the function body.


# 2. Defining a Function (Function Body):

# This indented block contains the actual code that the function executes when called.

# It can include statements, calculations, conditional logic, and loops.

# return statement (Optional): The return statement allows the function to send a
# value back to the caller line.
# This value becomes the output of the function call and need to be saved in a variable or used directly.

# Docstring is the and should be the first line in function body.


def greet(name):
  """Prints a greeting message."""

  print(f"Hello, {name} Welcome to python!")
  
  
greet("Pranit")  # Output: Hello, Pranit welcome to python!
#greet('Rohan')


def welcome(name) :
  """ Returns a greeting message to caller """

  return 'Hello' + name

msg = welcome('Pranit')

print(msg)

## PARAMETER VS ARGUMENT ##

# Parameters are variables used in function declaration.
# Arguments are values passed to the parameters in function call.


## TYPES OF ARGUMENTS ##

# Arguments: When calling a function, you provide actual values to match the
# parameters defined in the function signature.

# The number of arguments should match the number of parameters.

## 1. Positional Arguments ##

# Arguments are passed in the same order as the parameters.

def student(name, age):
    print(name, age)

student("Rahul", 20)


## 2. Default Arguments

# You can assign default values to parameters in the function declaration.

# If no argument is provided for a parameter when function is called then
# code will run with a default value,

# the default value is used.


def greet(name="World"):

    """
  This function greets a person by name.

  Args:
      name: The name of the person to greet. Defaults to "World".

  Returns:
      A string containing the greeting message.
  """

    return f"Hello, {name}!"

# Call the greet function with a specific name
print(greet("Alice"))

# Call the greet function with the default name
print(greet())


## 3. Keyword Arguments ##

# Keyword arguments, also known as named arguments, are a way to pass
# arguments to function's parameters during call by explicitly assigning
# arguments (values) with their parameter names.


def fullName(firstName,lastName):
    
    print(firstName + " " + lastName)


fullName( lastName = 'Newton', firstName = 'Issac' )


def calculate_area(length, width):
  
  return length * width


# Calling with keyword arguments (order doesn't matter)

area = calculate_area(width=5, length=3)

print(f"The area of the rectangle is {area}.")



# Benefits of Using Functions:

# Reusability: Functions can be used multiple times throughout your program -
# or even in other programs, saving time and effort.

# Write the code once, use it multiple times! Functions prevent repetitive code,
# saving time and effort.

def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

# Use the function for different rectangles
area1 = calculate_area(5, 3)  # Output: 15
area2 = calculate_area(10, 2)  # Output: