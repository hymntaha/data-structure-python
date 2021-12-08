def minWait(queries):
    if len(queries) == 0:
        return 0
    queries.sort()
    total = 0
    for index, duration in enumerate(queries):
        queriesLeft = len(queries) - (index+1)
        total += duration * queriesLeft

    return total


arr= [3,1,2,2,6]
print(minWait(arr))
