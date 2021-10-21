def printNums(low,up):
    if low > up:
        return

    print(low)
    return printNums(low+1,up)


print(printNums(1,5))
