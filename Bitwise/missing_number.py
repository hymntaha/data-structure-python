def find_missing_number(arr):
    n = len(arr) + 1

    #find sum all numbers from 1 to n.
    s1 = 0
    for i in range(1, n+1):
        s1 += i
    # substract all numbers in input from the sum
    for i in arr:
        s1 -= i


    #s1 is now the missing number

    return s1

arr= [1,5,2,6,4]
print(find_missing_number(arr))
