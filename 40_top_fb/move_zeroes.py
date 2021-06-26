def move_zeros_to_left(A):
    if len(A) < 1:
        return

    lengthA = len(A)
    write_index = lengthA - 1
    read_index = lengthA - 1

    while(read_index >= 0):
        if A[read_index] != 0:
            A[write_index] = A[read_index]
            write_index -= 1

        read_index -= 1

    while(write_index >= 0):
        A[write_index]=0;
        write_index-=1

nums=[1,10,20,0,59,63,0,88,0]
move_zeros_to_left(nums)
print(nums)
