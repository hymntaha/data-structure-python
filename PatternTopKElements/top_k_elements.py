from heapq import *

def find_k_largest_numbers(nums, k):
    minHeap = []
    # put first 'K' numbers in the min heap
    for i in range(k):
        heappush(minHeap, nums[i])

    # go through the remaining numbers of the array, if the number from the array is bigger than the
    # top(smallest) number of the min-heap, remove the top number from the heap and add the number from array
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    # the heap has the top 'K' numbers, return them in a list
    return list(minHeap)

def main():

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([11,3,5,14,16], 3)))

main()

"""
TIME COMPLEXITY: The time complexity of this algo is  O(K * logK + (N-K) * logK) which is asymptotically equal to O(N*logK)
SPACE COMPLEXITY: O(K)
"""
