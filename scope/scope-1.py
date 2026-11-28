import math

developerName = "Hemant"


def printGlobalVariable():
    print("Printing Global variable " + developerName)


def printLocalVariable():
    developerName = "Ajit"
    print("Printing Local variable " + developerName)

def printAndChangeGlobalVariable():
    global developerName
    developerName = "Jammy"
    print("Printing Global variable after changing value using global keyword " + developerName)

printLocalVariable()
printGlobalVariable()
printAndChangeGlobalVariable()