def can_reach_end(L):
    furthest_reach_so_far, last_index = 0, len(L) - 1,
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, L[i] + i)
        i+=1

    return furthest_reach_so_far >= last_index

a = [3,2,0,0,2,0,1]

print(can_reach_end(a))

"""
Time complexity: O(N)
Space complexity: O(1)
"""
