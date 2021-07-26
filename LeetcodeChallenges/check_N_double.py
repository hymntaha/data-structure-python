def checkIfExist(arr):
    cont=set()
    for i in range(len(arr)):
        if arr[i]*2 in cont or (arr[i]%2==0 and arr[i]//2 in cont):
            return True
        cont.add(arr[i])
    return False

nums = [-20,8,-6,-14,0,-19,14,4]
print(checkIfExist(nums))

def checkIfDoubleV2(arr):

    double = {}
    single = {}
    for num in arr:
        if num in double or num in single:
            return True
        else:
            double[num*2]=num
            single[num/2]=num

    return False

print(checkIfDoubleV2(nums))
