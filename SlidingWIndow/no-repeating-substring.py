def non_repeat_substring(str1):
    window_start = 0
    str_hash = {}
    str_length = 0

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in str_hash:
            window_start = max(window_start, str_hash[right_char]+1)

        str_hash[right_char] = window_end

        str_length = max(str_length, window_end-window_start+1)

    return str_length


print(non_repeat_substring('aabccbb'))

"""
TIME COMPLEXITY
Time complexity will be O(N), where 'N' is the number of characters in the input string.
SPACE COMPLEXITY
Space complexity will be O(K) where K is the number of distinct characters in the input string. 
"""
