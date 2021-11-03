def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    left, right = 0,1
    count = 0
    while right < len(intervals):
        print(intervals[left][1])
        if intervals[left][1] <= intervals[right][0]:
            left += 1
            right += 1
            count += 1
        else:
            left += 1
            right += 1

    if count == len(intervals) - 1:
        return True
    return False


def main():
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
