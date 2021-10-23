# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 2: return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b) % 10

        return b

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
