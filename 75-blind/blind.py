def isValid(s):
    stack = []
    closeToOpen = {'}':'{', ']':'[',')':'('}
    
    for c in s:
        if c in closeToOpen:
            print(stack[-1])
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
    return True if not stack else False


# print(isValid("([(){}])"))


def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l+r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1

# print(search([-1,0,3,5,9,12], 9))

def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bottom = 0, ROWS - 1

    while top <= bottom:
        mid = (top+bottom) // 2
        if target < matrix[mid][0]:
            bottom = mid - 1
        elif target > matrix[mid][-1]:
            top = mid + 1
        else:
            break

    if not top <= bottom:
        return False
    
    row = (top+bottom) // 2
    l, r = 0, COLS - 1

    while l <= r:
        mid = (l+r) // 2

        if matrix[row][mid] == target:
            return True
        if matrix[row][mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
