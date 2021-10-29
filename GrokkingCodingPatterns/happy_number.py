def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        if slow == fast:  # found the cycle
            break
    return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
    total = 0
    while (num > 0):
        digit = num % 10
        total += digit * digit
        num //= 10
    return total


print(find_happy_number(23))
print(find_happy_number(12))
''' 
Time complexity: The time complexity of the algorithm is diffucult 
to determine. However we know the fact that all unhappy number eventually
get stuck in the cycle:

4->16->37->58->89->145->42->20->4

This sequence behavior tells us 2 things:

1- If the number N is less than or equal to 1000, then we reach the cycle or 1 in at most 1001 steps.
2- For N > 1000, suppose the number has 'M' digits and the next number is N1. From the Wikipedia link, we know that 
the sum of the squares of the digits of N is at most 9^2M, or 81M (this will happen when all digits of N are 9.

This means:
N1 < 81M
As we know M = (logN+1)
Therefore N1 < 81 * log(N+1) => N1 = O(logN)

This concludes that the above algorithm will have a time complexity of O(logN)

Space Complexity:O(1)

'''
