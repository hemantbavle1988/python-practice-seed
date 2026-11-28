#Print without returning the value
def calculateAreaAndPrint(length,breadth):
    area = length * breadth
    print("Area is", area)

def calculateAreaAndReturn(length,breadth):
    area = length * breadth
    print("Returning area")
    return area


calculateAreaAndPrint(10,5)

print("Area is ", calculateAreaAndReturn(10,7))

print("Area with named parameters ", calculateAreaAndReturn(breadth=10,length=6))
