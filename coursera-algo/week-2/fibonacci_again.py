# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b) % m

    return b

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
