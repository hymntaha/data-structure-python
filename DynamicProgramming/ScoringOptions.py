def scoring_options(n):
    if n <= 0:
        return 0

    # Scoring options are 1,2 and 4

    # Max score is 4. Hence we need to save
    # last 4 ways to calculate the number of ways
    # for a given n
    # save the base case on last index of the vector

    result = [0,0,0,1]

    for i in range(1, n+1):
        current_sum = result[3] + result[2] + result[0]

        # slide left all the results in each iteration
        # result for current i will be saved at last index
        result[0] = result[1]
        result[1] = result[2]
        result[2] = result[3]
        result[3] = current_sum

    return result[3]

print(scoring_options(5))
