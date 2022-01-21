def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

print(singleNumber([4,1,2,3,4,2,1]))
