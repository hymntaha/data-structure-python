from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    
    # Calculate potential diners for segments between seated diners
    potential_diners = 0
    for i in range(1, M):
        gap = S[i] - S[i-1] - 1
        potential_diners += max(0, (gap - K) // (K+1))
    
    # Calculate potential diners before the first diner and after the last diner
    potential_diners += (S[0] - 1) // (K+1)
    potential_diners += (N - S[M-1]) // (K+1)
    
    return potential_diners



print(getMaxAdditionalDinersCount(10,1,2,[2,6])) # 3
# N = 15
# K = 2
# M = 3
# S = [11, 6, 14]
# print(getMaxAdditionalDinersCount(15, 2, 3, [11,6,14])) # 1

# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
#       [       ] [        ]     [ ]