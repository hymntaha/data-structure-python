"""
For index i, the water volume of i: vol_i = min(left_max_i, right_max_i) - bar_i.

The left_max array from left to right is always non-descending, the right_max is non-ascending.

Having such observation, we can say:

Given i < j, if left_max_i <= right_max_j: vol_i = left_max_i - bar_i, otherwise, vol_j = right_max_j - bar_j
because, if left_max_i <= right_max_j: left_max_i <= right_max_j <= right_max_j-1 <= ... <= right_max_i,
then min(left_max_i, right_max_i) is always left_max_i
"""
def trapWater(bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]
    while left < right:
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max:
            volume += l_max - bars[left]
            left += 1
        else:
            volume += r_max - bars[right]
            right -= 1
    return volume

block = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapWater(block))

##### other genius solution
def trapWater2(height):
    waterLevel = []
    left = 0
    for h in height:
        left = max(left, h)
        waterLevel += [left] # over-fill it to left max height
    right = 0
    for i, h in reversed(list(enumerate(height))):
        right = max(right, h)
        waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
    return sum(waterLevel)

print(trapWater2(block))
