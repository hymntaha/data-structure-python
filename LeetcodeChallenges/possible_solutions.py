def computeExpression(input, memo={}):
    if input.isdigit():
        return [int(input)]
    if input in memo:
        return memo[input]
    print(input)
    res = []
    for i in range(len(input)):
        if input[i] in "-+*":
            res1 = computeExpression(input[:i])
            res2 = computeExpression(input[i+1:])
            for j in res1:
                for k in res2:
                    res.append(mathOp(j, k, input[i]))
    memo[input] = res
    return res

def mathOp(m,n,op):
    if op == "+":
        return m+n
    elif op == "-":
        return m-n
    else:
        return m*n

print(computeExpression("2*3-4*5"))
