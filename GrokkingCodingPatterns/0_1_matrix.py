from collections import deque

def updateMatrix(matrix):
    # BFS Solution
    visited = set()
    q = deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                visited.add((i,j))
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
            newX, newY = x+dirr[0], y+dirr[1]
            if newX >= 0 and newX <= len(matrix)-1 and newY >= 0 and newY <= len(matrix[0])-1 and (newX, newY) not in visited:
                matrix[newX][newY] = matrix[x][y] + 1
                visited.add((newX, newY))
                q.append((newX, newY))
    return matrix

    # DP solution
    rows, cols = len(matrix), len(matrix[0])
    # Calculate the top/left adjacents
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != 0:
                top = matrix[row-1][col] if row > 0 else float('inf')
                left = matrix[row][col-1] if col > 0 else float('inf')

                martix[row][col] = min(top,left) + 1

    # Calculate the BOTTOM/RIGHT adjacent
    for row in range(rows)[::-1]:
        for col in range(cols)[::-1]:
            if matrix[row][col] != 0:
                bottom = matrix[row+1][col] if row<col-1 else float('inf')
                right = matrix[row][col+1] if col < cols else float('inf')

                matrix[row][col] = min(matrix[row][col], min(bottom, right)+1)

    return matrix
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat))
