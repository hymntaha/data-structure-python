def max_pairwise_product(numbers):
    first = 0
    second = 0

    for i in numbers:
        if i > first:
            first = i

    for i in numbers:
        if i > second and i != first:
            second = i

    return first * second


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
