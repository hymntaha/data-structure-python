def getSum(a,b):
    x, y = abs(a), abs(b)

    # Ensure x >= y
    if x < y:
        return getSum(b,a)
    sign = 1 if a > 0 else -1

    if a * b >= 0:
        # Sum of 2 pos integers
        while y:
            x, y = x ^ y, (x & y) << 1
    else:
        # difference of 2 pos integers
        while y:
            x,y = x ^ y, ((~x) & y) << 1
    return x * sign

x = 2
y = 1
print(getSum(2,1))
