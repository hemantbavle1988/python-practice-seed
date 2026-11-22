
# Variable Assignment and String Formatting
# Assignment 1
name = "Hemant"
age = 37
city = "Pune"

print("Using string concatenation:")
print("My name is " + name + ", I am " + str(age) + " years old and I live in " + city + ".")

print(f"Using f-strings:")
print(f"My name is {name}, I am {age} years old and I live in {city}.")

print("\n")
print("Using command line input:")
input_name = input("Enter your name: ")
input_age = int(input("Enter your age: "))
input_city = input("Enter your city: ")

print("Using string concatenation:")
print("Hello " + input_name + ", you are " + str(input_age) + " years old and you live in " + input_city + ".")

print("Using f-strings:")
print(f"Hello {input_name}, you are {input_age} years old and you live in {input_city}.")


# Assignment 2
input_fav_color = input("Enter your favorite color: ")
input_fav_food = input("Enter your favorite food: ")
input_fav_movie = input("Enter your favorite movie: ")

print("Using string concatenation:")
print("My favorite color is " + input_fav_color + "\n My favorite food is " + input_fav_food + "\n My favorite movie is " + input_fav_movie + ".")
print("Using f-strings:")
print(f"My favorite color is {input_fav_color}\n My favorite food is {input_fav_food}, \n My favorite movie is {input_fav_movie}.")



# Assignment 3
first_variable = "Python"
second_variable = "is"
third_variable = "awesome"

print("Using Separator:")
print(first_variable, second_variable, third_variable, sep="|")