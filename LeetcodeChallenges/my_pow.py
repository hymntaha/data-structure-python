def myPow(x,n):
    if n < 0:
        x = 1/x
        n = -n
    ans = 1
    while n :
        if n % 2:
            ans = x * ans
            n -= 1
        else:
            x = x * x
            n = n // 2
    return ans

x = 2.0000
b = -3
print(myPow(x,b))

"""
Time complexity: O(logn)
Space complexity: O(1)
"""

