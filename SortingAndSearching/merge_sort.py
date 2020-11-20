def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr) // 2 # Mid of the arr
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        # Initializing index variables
        j=0
        i=0
        k=0

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j<len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [3,2,1,5,4]
merge_sort(arr)

print(arr)

""" Time complexity = O(nlogn)"""
