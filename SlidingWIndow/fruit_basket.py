def fruits_into_baskets(fruits):
    max_fruits = 0
    fruit_basket = {}
    window_start = 0

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]

        if right_fruit not in fruit_basket:
            fruit_basket[right_fruit] = 0
        fruit_basket[right_fruit] += 1

        while len(fruit_basket) > 2:
            left_fruit = fruits[window_start]
            fruit_basket[left_fruit] -= 1
            if fruit_basket[left_fruit] == 0:
                del fruit_basket[left_fruit]

            window_start += 1
        max_fruits = max(max_fruits, window_end-window_start+1)
    return max_fruits

    return max_fruits


fruits=['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(fruits))

# time complexity is O(N) where N is the number of chars in the input array.
# The outer for loop runs for all chars and the inner while loop processes each character only once, therefore, the time complexity of the algo is O(N+N)
# which is asymptotically equivalent to O(N)
# Space complexity - constant - O(1) as there can be a max of three types of fruits stored in frequency map.
