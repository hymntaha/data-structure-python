def maxProfit(price):
    maxProf = 0
    l, r = 0, 1

    while r < len(price) - 1:
        if price[l] < price[r]:
            profit = price[r] - price[l]
            maxProf = max(maxProf, profit)
        else:
            l = r
        r += 1

    return maxProf


prices = [7,1,5,3,6,4]
print(maxProfit(prices))
