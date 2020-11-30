def fib(num, lookup_table):
    if lookup_table[num] == -1: # Check if already present

        # Adding entry to table when not present
        if num <=1:
            lookup_table[num] = num
        else:
            lookup_table[num] = fib(num - 1, lookup_table) + fib(num-2, lookup_table)

    return lookup_table[num]


num = 6  # Finding the nth Fibonacci number
lookup_table = [-1] * (num + 1)  # Initializing the lookup table to have -1 of size num + 1
print(fib(num, lookup_table))
