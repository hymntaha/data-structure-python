def getNthFib(n):
    lastTwo = [0,1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

'''
Time complexity: O(n)
Space complexity: O(1)
'''

##### Memoized version #######
def getNthFib(n, memo={1:0, 2:1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = getNthFib(n-1, memo) + getNthFib(n-2, memo)
    return memo[n]
