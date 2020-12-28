class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def print_interval(self):
        print("[" + str(self.start) + ', ' + str(self.end) + "]", end='')

def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x:x.start)

    merged = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1,len(intervals)):
        interval = intervals[i]
        if interval.start <= end: # overlapping intervals, adjust the end
            end = max(interval.end, end)
        else: # non-overlapping interval, add the previous interval and reset
            merged.append(Interval(start,end))
            start = interval.start
            end = interval.end
    merged.append(Interval(start, end))
    return merged

print("Merged intervals: ", end='')
for i in merge_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
print()

# Time complexity: O(N * logN) where N is tthe total number of intervals. Iterating the intervals only once will take O(N),
# in the beginning though, since we need to sort the intervals, algorithm will take O(N*logN)
# Space complexity: O(N) for sorting
