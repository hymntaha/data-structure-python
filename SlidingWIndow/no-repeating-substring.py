def non_repeat_substring(str1):
    window_Start = 0
    max_length = 0
    char_index_map = {}

    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str1)):
        right_char = str1[window_Start]
        if right_char in char_index_map:
            # this is tricky, in the current window, we will not have any 'right char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char' we will keep 'window_start'
            window_Start = max(window_end, char_index_map[right_char]+1)

        # insert the 'right_char' into the map
        char_index_map[right_char] = window_end
        # remember the max length so far
        max_length = max(max_length, window_end-window_Start+1)
    return max_length


print(non_repeat_substring('aabccbb'))
