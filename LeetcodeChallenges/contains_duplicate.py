def containsDuplicate(nums):
        hash = {}

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        for i, j in hash.items():
            if j > 1:
                return True

        return False


nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
