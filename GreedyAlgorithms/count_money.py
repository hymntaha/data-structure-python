def find_min_coins(v, coins_available):
    result = []
    n = len(coins_available)

    # Traverse through all available coins
    for i in reversed(range(n)):
        while v >= coins_available[i]:
            v -= coins_available[i]
            result.append(coins_available[i])
    return result

v = 19
available_coins = [1, 5, 10, 25]
print(find_min_coins(v, available_coins))

# Since there is a nested loop, the while loop inside a for loop, the time complexity is O(N^2)
