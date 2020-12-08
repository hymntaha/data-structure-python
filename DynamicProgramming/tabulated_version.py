# Time complexity of this is linear O(n) since the for loop runs n - 2 times. This, again, is a significant improvement over the exponential time
def fib(num, lookup_table):
    # Set 0th and first values
    lookup_table[0] = 0
    lookup_table[1] = 1

    for i in range(2, num+1):
        # Fill up the table by summing up previous two values
        lookup_table[i] = lookup_table[i-1]+lookup_table[i-2]

    return lookup_table[num] # Return the nth Fib num


num = 6
lookup_table = [0] * (num + 1)
# print(fib(num, lookup_table))


####### Tabulated version #2
# Time complexity is also linear O(n) since the for loop runs n - 2 times.
# It is not only an improvement over the recursive non-dynamic implementation over
# 1st solution owing to the reduced space complexity
def fib(num):
    if num == 0:
        return 0

    current = 0
    second_last = 0
    last = 1

    for i in range(2, num+1):

        current, second_last = second_last+last, last
        last = current

    return current

num = 6
print(fib(num))
