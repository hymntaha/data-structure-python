def twoSum(numbers, target):
    start, end = 0, len(numbers)-1

    while start<end:
        sum = numbers[start]+numbers[end]

        if sum == target:
            break
        elif sum > target:
            end-=1
        else:
            start+=1

    return [start+1, end+1]

arr = [2,7,11,15]
tar = 18
print(twoSum(arr,tar))
