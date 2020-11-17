def optimal_task(arr):
    arr.sort()
    for i in range(len(arr)//2):
        print(arr[i], arr[~i])


print(optimal_task([6, 3, 2, 7, 5, 5]))
