def fruits_into_baskets(fruits):
    max_fruits = 0
    window_start = 0
    fruit_freq = {}

    for window_end in range(len(fruits)):
        right_char = fruits[window_end]
        if right_char not in fruit_freq:
            fruit_freq[right_char] = 0
        fruit_freq[right_char] += 1

        while len(fruit_freq) > 2:
            left_char = fruits[window_start]
            window_start += 1
            fruit_freq[left_char] -= 1
            if fruit_freq[left_char] == 0:
                del fruit_freq[left_char]

        max_fruits = max(max_fruits, window_end-window_start+1)

    return max_fruits


fruits=['A', 'B', 'C', 'B', 'B', 'C']
print(fruits_into_baskets(fruits))
