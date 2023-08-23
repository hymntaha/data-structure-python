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


