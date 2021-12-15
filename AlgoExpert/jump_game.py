def jumpGame(array):
    goal = len(array) - 1

    for i in range(len(array) - 1, -1, -1):
        if i + array[i] >= goal:
            goal = i

    return True if goal == 0 else False



print(jumpGame([3,2,1,0,4]))
