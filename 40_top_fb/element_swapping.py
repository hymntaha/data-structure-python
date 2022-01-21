import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

'''
Setup our multi-sig wallet and build out our in-app on-chain treasury + voting system where users can create proposals, vote, etc. We have over $100,000 in our treasury right now, but, haven’t set up a voting system!
Build a “Connect to Wallet” button for us that allows users to sign-in with either Ethereum, Solana, Polygon, and AVAX.
Build our out PFP NFT drop. Find an artist, generate the collection, give users a web app they can use to mint their NFT on Polygon where we’d pay their gas fee. Ship the whole thing end-to-end.
Hardhat, Remix, Infura, and Alchemy
Experience working with Solidity.
Experience with documenting distributed application business logic and workflow.
Proficient in preparing smart contract tests (using mocha) to cover all possible edge cases and scenarios.
Technical knowledge of the main blockchain protocols, consensus mechanisms and latest innovations in the space (i.e. zk-SNARKs, Compound, Yield farming, Ethereum 2.0).
Deep understanding of blockchain fundamentals (smart contracts, web3, DAOs, Wallets, payment gateways, exchanges).
Experience operating blockchain nodes especially in Ethereum.
Knowledgeable about smart contract security and best practices (design patterns).
'''


def findMinArray(arr, k):
    # return array itself if size 1 or empty
    if len(arr) < 2:
        return arr
    # Start from end of array, choose the element that is smaller that the first element and can make it to the beginning (i <= k)
    i = len(arr) - 1
    while i >= 0 and k > 0:
        if arr[i] < arr[0] and i <= k:
            # pop the candidate element and insert it to the beginning
            val = arr.pop(i)
            arr = [val] + arr
            # reduce the k, i number of times and go one step backward (i -= 1)
            k -= i
            i -= 1
        else:
            i -= 1
    return arr


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')

def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')

test_case_number = 1

def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1

if __name__ == "__main__":
    # n_1 = 3
    # arr_1 = [5, 3, 1]
    # k_1 = 2
    # expected_1 = [1, 5, 3]
    # output_1 = findMinArray(arr_1,k_1)
    # check(expected_1, output_1)

    n_2 = 5
    arr_2 = [8, 9, 11, 2, 1]
    k_2 = 2
    expected_2 = [2, 8, 9, 11, 1]
    output_2 = findMinArray(arr_2,k_2)
    check(expected_2, output_2)

    # Add your own test cases here

