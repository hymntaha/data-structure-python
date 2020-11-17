def array_advance(A):
    idx = 0
    furthest_idx = 0
    while idx <= furthest_idx and furthest_idx <= len(A) - 1:
        furthest_idx = max(furthest_idx, A[idx]+idx)
        idx += 1

    return furthest_idx >= len(A) - 1



# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# # False: Not possible to navigate to last index in A:
# A = [3, 2, 0, 0, 2, 0, 1]
# print(array_advance(A))
