def find_largest_number(number_of_digits, sum_of_digits):
    # If the sum of digits is 0, then a number is possible only if the number of digits is 1.
    if sum_of_digits == 0:
        if number_of_digits == 1:
            return [0]
        else:
            return [-1]

    # sum_of_digits is greater than the max possible sum.
    if sum_of_digits > 9 * number_of_digits:
        return [-1]

    result = [0] * number_of_digits

    # Fill from most significant digit to least significant digit!
    for i in range(number_of_digits):

        # place 9 to make the number largest
        if sum_of_digits >= 9:
            result[i] = 9
            sum_of_digits -=9

        # If remaining sum becomes less than 9, then fill the remaining sum
        else:
            result[i] = sum_of_digits
            sum_of_digits = 0
    return result



sum_of_digits = 20
number_of_digits = 3

print(find_largest_number(number_of_digits, sum_of_digits))
# result = [9, 9, 2]

# The time complexity is O(n) bc we can simply find the solution in one iteration
