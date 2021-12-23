def gcd(testVariable1, testVariable2) :
    # Base Case
    if testVariable1 == testVariable2 :
        return testVariable1

    # Recursive Case
    if testVariable1 > testVariable2 :
        return gcd(testVariable1 - testVariable2, testVariable2)
    else :
        return gcd(testVariable1, testVariable2 - testVariable1)

# Driver Code
number1 = 6
number2 = 9
print(gcd(number1, number2))
