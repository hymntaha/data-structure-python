def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x:x[1],reverse=1)
    s=0
    for i,j in boxTypes:
        i=min(i,truckSize)
        s+=i*j
        truckSize-=i
        if truckSize==0:
            break
    return s


boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(maximumUnits(boxTypes, truckSize))

