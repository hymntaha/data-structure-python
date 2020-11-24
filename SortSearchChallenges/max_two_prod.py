from decimal import Decimal

def find_max_prod(lst):
    # sorted_lst = sorted(lst)
    # return  sorted_lst[-2], sorted_lst[-1]

    max1 = lst[0]
    max2 = Decimal('-Infinity')

    min1 = lst[0]
    min2 = Decimal('Infinity')

    for number in lst:

        if number > max1:
            max2 = max1 # second highest
            max1 = number # first highest

        elif number > max2:
            max2 = number

        if number < min1:
            min2 = min1 # Second lowest
            min1 = number # First lowest
        elif number < min2:
            min2 = number

        if max1 * max2 > min1 * min2:
            return max2, max1
        else:
            return min2, min1


lst = [1, 3, 5, 2, 6]
print(find_max_prod(lst))

# We have traversed the list in a single loop. So, the time complexity is O(n)
