from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  sum = R * C
  count = 0
  for i in range(len(G)):
    for j in range(len(G[i])):
      if G[i][j] == 1:
        count += 1

  return count/sum


print(getHitProbability(2, 3,[[0,0,1],[1,0,1]]))