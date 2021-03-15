from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if(len(intervals) < 2):
        return intervals

    intervals.sort(key=lambda x:x.start)

    merged = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1,len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged.append(Interval(start,end))
            start = interval.start
            end = interval.end
    merged.append(Interval(start,end))
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(0, 4)]):
        i.print_interval()
    print()

main()
