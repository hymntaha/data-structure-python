def twoSum(nums, target):
    hash = {}


    for i in range(len(nums)):
        remain = target - nums[i]
        if remain in hash:
            return [i, hash[remain]]
        hash[nums[i]] = i

lst = [3,2,4]
tar = 6
print(twoSum(lst,tar))

