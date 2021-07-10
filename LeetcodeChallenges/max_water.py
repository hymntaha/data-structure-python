def getMaxContainer(water):
    indexA =0
    indexB = len(water) - 1
    maxArea = 0

    while indexA < indexB:
        minIndex = min(water[indexA], water[indexB])
        maxArea = max(maxArea, minIndex * (indexB - indexA))

        if water[indexA] < water[indexB]:
            indexA += 1
        else:
            indexB -= 1

    return maxArea

arr = [4,8,1,9,3,11]
print(getMaxContainer(arr))
