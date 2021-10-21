# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 1

    current, prev1, prev2 = 0,1,1
    for i in range(3, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return current

# n = int(input())
print(calc_fib(10))

# 1 1 2 3 5
