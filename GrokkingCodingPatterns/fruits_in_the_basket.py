def fruits_in_the_basket(fruits):
    max_fruits = 0
    window_start = 0
    fruit_basket = {}

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_basket:
            fruit_basket[right_fruit] = 0
        fruit_basket[right_fruit] += 1

        if len(fruit_basket) > 2:
            left_fruit = fruits[window_start]
            fruit_basket[left_fruit] -= 1

            if fruit_basket[left_fruit] == 0:
                del fruit_basket[left_fruit]
            window_start += 1
        max_fruits = max(max_fruits, window_end - window_start +1)
    return max_fruits


fru = ['A', 'B', 'C', 'B', 'B', 'C']
print(fruits_in_the_basket(fru))
