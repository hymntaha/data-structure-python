# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to < 2: return to
    else:
        a, b = 0, 1
        for i in range(from_, to):
            a, b = b, (a+b) % 10

        return b


if __name__ == '__main__':
    # input = sys.stdin.read();
    # from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(10, 200))
