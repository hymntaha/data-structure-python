import heapq

def kClosest(points, K):
    heap = []
    for (x,y) in points:
        dist = -(x*x + y*y)
        if len(heap) == K:
            heapq.heappushpop(heap,(dist,x,y))
        else:
            heapq.heappush(heap,(dist,x,y))

    return [(x,y) for (dist,x,y) in heap]



points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points,k))

"""
Inserting an item to a heap of size k take O(logK) time.
And we do this for each item points.
So runtime is O(N*logK) where N is the length of points.

Space: O(K) for our heap
"""
