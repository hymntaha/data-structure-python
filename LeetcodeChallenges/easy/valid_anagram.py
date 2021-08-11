def isAnagram(s,t):
    new_string = {}

    for i in s:
        if i in new_string:
            new_string[i] += 1
        else:
            new_string[i] = 1

    for i in t:
        if i in new_string:
            new_string[i] -= 1
        else:
            return False

    for i in new_string.items():
        if i[1] != 0:
            return False

    return True


s = 'rat'
t = 'car'

print(isAnagram(s,t))
"""
Time complexity = O(N)
Space complexity = O(N)
"""
