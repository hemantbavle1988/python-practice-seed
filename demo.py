print("Hello there! This is a demo script. Learning python is fun!")

someNumber = 10;

someDecimal = 3.14;

someString = "This is a string variable."

someBoolean = True;

someList = [1, 2, 3, 4, 5];

someTuple = (1, 2, 3, 4, 5);

someDictionary = {"key1": "value1", "key2": "value2", "key3": "value3"};

someSet = {1, 2, 3, 4, 5};

someNone = None;

someComplex = 1 + 2j;



print("The value of someNumber is:", someNumber, type(someNumber));
print("The value of someDecimal is:", someDecimal, type(someDecimal));
print("The value of someString is:", someString, type(someString));
print("The value of someBoolean is:", someBoolean, type(someBoolean));
print("The value of someList is:", someList, type(someList));
print("The value of someTuple is:", someTuple, type(someTuple));
print("The value of someDictionary is:", someDictionary, type(someDictionary));
print("The value of someSet is:", someSet, type(someSet));
print("The value of someNone is:", someNone, type(someNone));
print("The value of someComplex is:", someComplex, type(someComplex)); 
# This is a single line comment
print("After a single line comment, the code continues to execute.")

"""
print("After a single line comment, the code continues to execute.")

This is a multi-line comment.

It can span multiple lines.

"""
print("After a multi-line comment, the code continues to execute.")



# Type casting

#Numbers and floats
numA = 20;
numB = 2.5;
numCC1 = 3.6;

numC = numA + numB;
numD = float(numA) + int(numB);
numE = str(numA) + str(numB);
numF = int(numA) + int(numB);
numG = bool(abs(numA));

print("The value of numC is:", numC, type(numC));
print("The value of numD is:", numD, type(numD)); 
print("The value of numE is:", numE, type(numE));
print("The value of numF is:", numF, type(numF));
print("The value of numG is:", numG, type(numG));

numH = int(numCC1);
print("The value of numH is:", numH, type(numH));

numI = float(numH);
print("The value of numI is:", numI, type(numI));

numJ = str(numI);
print("The value of numJ is:", numJ, type(numJ));

numK = bool(numJ);
print("The value of numK is:", numK, type(numK));

numL = int("20") * numCC1;
print("The value of numL is:", numL, type(numL));

#Strings
strA= "20";
strB= "2.5";


strC = strA + strB;
strD = int(strA) + float(strB);
strE = str(int(strA) + float(strB));
strF = bool(strA);
print("The value of strC is:", strC, type(strC));
print("The value of strD is:", strD, type(strD));   
print("The value of strE is:", strE, type(strE));
print("The value of strF is:", strF, type(strF));