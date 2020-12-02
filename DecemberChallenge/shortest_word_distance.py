def shortestDistance(words, word1, word2):
    size = len(words)
    index1, index2 = size, size
    ans = size

    for i in range(size):
        if words[i] == word1:
            index1 = i
            ans = min(ans, abs(index1-index2))
        elif words[i] == word2:
            index2 = i
            ans = min(ans, abs(index1-index2))
    return ans

word1 = "makes"
word2 = "coding"
words = ["practice", "makes", "perfect", "coding", "makes"]
print(shortestDistance(words, word1, word2))
