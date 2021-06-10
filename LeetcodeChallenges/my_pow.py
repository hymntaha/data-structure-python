def myPow(x,n):
    if n < 0:
        x = 1 / x
        n = -n

    pow = 1

    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow

x = 2.0000
b = -3
print(myPow(x,b))
