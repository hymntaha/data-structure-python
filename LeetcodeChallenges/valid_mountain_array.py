def validMountain(A):
    N = len(A)
    i = 0

    # walk up
    while i+1 < N and A[i] < A[i+1]:
        i += 1

    # peak can't be first or last
    if i == 0 or i == N-1:
        return False

    # walk down
    while i+1 < N and A[i] > A[i+1]:
        i += 1

    return i == N-1

arr=[0,2,3,4,5,2,1,0]
# arr =[0,3,2,1]
print(validMountain(arr))
