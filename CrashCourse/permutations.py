def permutations(l):
    def dfs(path,used,res):
        if len(path) == len(l):
            res.append(path[:]) # note [:] make a deep copy since otherwise we'd append the same list over and over
            return

        for i, letter in enumerate(l):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used,res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    res = []
    dfs([], [False] * len(l), res)
    return res

inputs = ["ab", "abc"]
for i in range(len(inputs)):
    print("Permutations :",permutations(inputs[i]))
