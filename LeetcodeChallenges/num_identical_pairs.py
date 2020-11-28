def numIdenticalPairs(nums):
    hashMap = {}
    res = 0
    for number in nums:
        if number in hashMap:
            res += hashMap[number]
            hashMap[number] += 1
        else:
            hashMap[number] = 1
    return res


nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))

# 1 2 3 1 1 3
# ^ ^
