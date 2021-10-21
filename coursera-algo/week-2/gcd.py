# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    absolute_prod = abs(a*b)

    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if((greater % a ==0 ) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1

    return absolute_prod/lcm

if __name__ == "__main__":
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    print(gcd_naive(216,234))

'''



'''
