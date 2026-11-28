x = "Global Scope"

def printGlobal():
    print(x)


def printEnlcosingAndLocalScope():
    x = "Enclosing Scope"

    def printLocalScope():
        x ="Local Scope"
        print(x)

    printLocalScope()

    print(x)



def printUsingNonLocalScope():
    # This line is compulsory for using "nonlocal keyword, else the
    # code will fail with no binding for nonlocal x found" error
    x= "Enclosing Scope(Non local example)"
    print("Before Nonlocal:", x)
    def printLocalScope():
        nonlocal x
        x ="Non Local Scope"
        print(x)

    printLocalScope()

printEnlcosingAndLocalScope()
printUsingNonLocalScope()
printGlobal()
