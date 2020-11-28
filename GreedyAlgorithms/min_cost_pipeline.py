def min_cost(pipes):
    cost = 0
    n = len(pipes)
    pipes.sort() # Sorting the list using the .sort() built-in function

    for i in range(n-1):
        prev_cost = cost # store previos cost for later use
        cost = (pipes[i]+pipes[i+1]) # find current cost
        pipes[i+1] = cost # insert in list

        cost = cost +prev_cost # add with previous cost

    return cost


pipes = [4, 3, 2, 6]
print(min_cost(pipes))

# The time complexity for this solution is O(nlogn), because of the use of sort function.
