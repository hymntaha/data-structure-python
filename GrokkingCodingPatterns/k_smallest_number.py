from heapq import *


def find_Kth_smallest_number(nums, k):
    maxHeap = []
    # put first k numbers in the max heap
    for i in range(k):
        heappush(maxHeap, -nums[i])

    # go through the remaining numbers of the array, if the number from the array is smaller than the
    # top(biggest) number of the heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    # the root of the heap has the Kth smallest number
    return -maxHeap[0]


def main():

    # print("Kth smallest number is: " +
    #       str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    # print("Kth smallest number is: " +
    #       str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
