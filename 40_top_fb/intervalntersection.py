def intervalInterSection(firstList, secondList):
    output = []
    i, j = 0,0

    while i < len(firstList) and j < len(secondList):
        lo = max(firstList[i][0], secondList[j][0])
        hi = min(firstList[i][1], secondList[j][1])

        if lo <= hi:
            output.append([lo,hi])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return output

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(intervalInterSection(firstList, secondList))
