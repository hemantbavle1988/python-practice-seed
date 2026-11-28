def printMessageWithoutDefaultVal(name):
    print("Hello " + name)

printMessageWithoutDefaultVal("Hemant")

def printMessageWithDefaultVal(name="Hemant"):
    if name == "Hemant":
        print("Printing Default Value")
    else:
        print("Printing argument Value")
    print("Hello " + name)

printMessageWithDefaultVal("Mugdha")
printMessageWithDefaultVal()


