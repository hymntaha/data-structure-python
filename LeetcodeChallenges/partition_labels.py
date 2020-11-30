def partitionLabels(S):
    result,last_seen, max_last_seen, count = [], {}, 0, 0
    for i, char in enumerate(S):
        last_seen[char]=i
    for i,char in enumerate(S):
        max_last_seen = max(max_last_seen, last_seen[char])
        count += 1
        if i == max_last_seen:
            result.append(count)
            count = 0

    return result

S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))


# Space O(1) bc the max number of entries is 26 in the dict (one per letter). So the dict size does not increase with N.
