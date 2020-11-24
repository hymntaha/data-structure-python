# Decimal library to assign infinite numbers
from decimal import Decimal

def find_max_prod(lst):
    max1 = lst[0]
    max2 = Decimal('-Infinity')

    min1 = lst[0]
    min2 = Decimal('Infinity')

    for number in lst:

        if number > max1:
            max2 = max1  # Second highest
            max1 = number  # First highest
        elif number > max2:
            max2 = number

        if number < min1:
            min2 = min1  # Second lowest
            min1 = number  # First lowest
        elif number < min2:
            min2 = number

    # Checking which pair has the highest product
    if max1 * max2 > min1 * min2:
        return max2, max1
    else:
        return min2, min1


# lst = [1, 3, 5, 2, 6]
# num1, num2 = find_max_prod(lst)
# print(num1, num2)

lst = [1, -3, -5, 2, 6]
num1, num2 = find_max_prod(lst)
print(num1, num2)

# We have traversed the list in a single loop. So, the time complexity is O(n)
