def rearrange(lst):
    result = []

    for i in lst:
        if i < 0:
            result.append(i)

    for i in lst:
        if  i >= 0:
            result.append(i)
    return result

# print(rearrange([10,-1,20,4,5,-9,-6]))

def rearrangeInPlace(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if (lst[curr] < 0):
            # if not the last negative number
            if (curr is not leftMostPosEle):
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst


print(rearrangeInPlace([10, -1, 20, 4, 5, -9, -6]))
