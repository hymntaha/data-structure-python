import heapq
def findKthLargest(nums, k):
    if not nums or not k or k < 0:
        return None

    maxHeap, res = [], None
    for num in nums:
        heapq.heappush(maxHeap, -num)

    for _ in range(k):
        res = -heapq.heappop(maxHeap)
    return res


nums = [8,5,6,1,3,4,2]
k = 3

print(findKthLargest(nums,k))

"""
Space comp: O(N)
Time comp: O(N + klogn) -----> N is the loop, k is how many times we pop, logn heapify
"""
