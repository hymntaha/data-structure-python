def search_next_letter(letters, key):

    n = len(letters)
    if key > letters[n-1]:
        return letters[0]

    l,h = 0, n - 1
    while l <= h:
        mid = l+(h-l) // 2
        if key < letters[mid]:
            h = mid - 1
        else:
            l = mid + 1

    return letters[l % n]



def main():
    # print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    # print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
