import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
    result = []
    dict = {}
    largestK = 0
    for i in range(len(points)):
        total = (points[i].x * points[i].x) + (points[i].y * points[i].y)
        dict[abs(total)] = [points[i].x, points[i].y]

    print(dict)
    return result


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
