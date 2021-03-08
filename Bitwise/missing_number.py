def find_missing_number(arr):
    n = len(arr) + 1

    #find sum all numbers from 1 to n.
    s1 = 0
    for i in range(1, n+1):
        s1 += i
    # substract all numbers in input from the sum
    for i in arr:
        s1 -= i


    #s1 is now the missing number

    return s1

arr= [1,5,2,6,4]
print(find_missing_number(arr))

"""
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)

What could go wrong with the above algorithm?
While finding the sum of numbers from 1 to n, we can integer overflow when n is large.
"""

######## BITWISE APPROACH
def find_missing_number_bitwise(arr):
    n = len(arr) - 1
    x1 = 1
    # x1 represents XOR of all values from 1 to n
    for i in range(2, n+1):
        x1 = x1 ^ i

    # x2 represents XOR of all values in arr
    x2 = arr[0]
    for i in range(1, n-1):
        x2 = x2 ^ arr[i]

    # missing number is the xor of x1 and x2
    return x1 ^ x2

"""
Taking XOR of a number with itself returns 0, e.g.,

1 ^ 1 = 0
29 ^ 29 = 0

Taking XOR of a number with 0 returns the same number, e.g.,

1 ^ 0 = 1
31 ^ 0 = 31

XOR is Associative & Commutative, which means:

(a ^ b) ^ c = a ^ (b ^ c)
a ^ b = b ^ a
"""
