def isAlienSorted(words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dict = {}
        new_words = []

        for i,c in enumerate(order):
            dict[c] = i

        for word in words:
            new = []
            for c in word:
                new.append(dict[c])
            new_words.append(new)

        for w1,w2 in zip(new_words,new_words[1:]):
            if w1 > w2:
                return False

        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
