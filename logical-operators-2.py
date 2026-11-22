a = 10
b = 10
c = b
print("c is a :",c is a)

print("c is a :",c is not a)

flag = True if(a >= 10 and b <= 10) else False
if flag:
    print("Both conditions are True")
else:
    print("One or both conditions are False")





age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")