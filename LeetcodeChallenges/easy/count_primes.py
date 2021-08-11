from math import sqrt


def countPrimes(n: int) -> int:
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(sqrt(n) + 1)):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    print(is_prime)
    return is_prime.count(True)

n = 10
print(countPrimes(n))
