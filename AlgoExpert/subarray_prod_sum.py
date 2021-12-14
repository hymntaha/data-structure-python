def prodSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum = prodSum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier

'''
Time: O(N) Every single element and sub array
Space: O(D) Depth of the recursion
'''
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(prodSum(array))
