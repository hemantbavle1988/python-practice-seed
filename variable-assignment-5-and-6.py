from os import name


first_name=input("Enter your name: ")
last_name=input("Enter your last name: ")
print("Using separator:")
print("My name is ",first_name,last_name,sep="|", end="###\n")
print("I am learning Python programming language.")
print("Pythong is interesting and fun to learn.")



"""
name - valid
2name - not valid
first_name - valid
first name - not valid
student123 - valid
class - not valid
my-name - not valid
_age - valid
total_cost - valid
"""