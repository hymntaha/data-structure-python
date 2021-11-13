def find_missing_number(nums):
    s = 0
    n = len(nums) + 1

    for i in range(1, n + 1):
        s += i

    for j in nums:
        s -= j

    return s
def main():
    arr = [1, 5, 2, 6, 4]
    print('Missing number is:' + str(find_missing_number(arr)))

main()
