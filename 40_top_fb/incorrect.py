def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
    expectedVal = ''
    for i in range(N):
        if C[i] == 'A':
            expectedVal += 'B'
        else:
            expectedVal += 'A'
            
    return expectedVal



print(getWrongAnswers(6, 'AAAAAA'))
print(getWrongAnswers(3, 'BAB'))