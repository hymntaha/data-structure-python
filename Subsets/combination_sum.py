def combinationSum(candidates,target):
    # res = []
    #
    # def dfs(i,cur,total):
    #     if total == target:
    #         res.append(cur.copy())
    #         return
    #     if i >= len(canditates) or total > target:
    #         return
    #
    #     cur.append(canditates[i])
    #     dfs(i, cur, total + canditates[i])
    #     cur.pop()
    #     dfs(i+1, cur,total)
    # dfs(0, [], 0)
    # return res

    # def combinationSum(candidates, target):
        # Edge Case
        if not candidates:
            return []

        # Define recursive function
        def rc(nums, target):
            nonlocal low_num
            combos = []
            for i in range(len(nums)-1, -1, -1):
                cur_val = nums[i]
                if cur_val == target:
                    combos.append([target])
                elif cur_val + low_num > target:
                    # Don't waste time processing sub_combos for a number too large to be in any
                    continue
                else:
                    # Pass the list including current value into function to get all combos for sub-target.
                    sub_combos = rc(nums[:i+1], target - cur_val)
                    # Now add the current value to all of those combinations.
                    for sub in sub_combos:
                        sub.append(cur_val)
                        combos.append(sub)
            return combos

        candidates.sort()   # The problem didn't specify that candidates would be ordered.
        low_num = candidates[0]    # Used in rc to stop processing values that won't be in any subgroup
        return rc(candidates, target)


arr = [2,3,5,7]
target = 7

print(combinationSum(arr,target))
