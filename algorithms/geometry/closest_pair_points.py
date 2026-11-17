# The closest pair of points problem finds two points in a 2d plane that are closest
# to each other based on their euclidean distance.

# It's an important computational geometry problem solved efficiently using
# divide and conquer technique.

# Explanation

# A naive approach compares every pair of points - taking O(n * n) time.
# But with divide and conquer we can reduce the time complexity to O(n log n).

# Steps:

# Sort the points based on their x - coordinates.
# Divide the set of points into two halves (left and right).
# Recursively find the smallest distance in each half.
# Combine the results - check for closer pairs that lie across the dividing line using a strip region
# Return the minimum of all distances found.

import math


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def bruteforce(points):
    n = len(points)

    min_d = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            min_d = min(d, min_d)
    return min_d


def strip_closest(strip, d):
    min_d = d
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_d:
            min_d = min(min_d, dist(strip[i], strip[j]))
            j += 1
    return min_d


def closest_util(points):
    n = len(points)
    if n <= 3:
        return bruteforce(points)

    mid = n // 2
    mid_point = points[mid]

    dl = closest_util(points[:mid])
    dr = closest_util(points[mid:])
    d = min(dl, dr)

    strip = [p for p in points if abs(p[0] - mid_point[0]) < d]

    return min(d, strip_closest(strip, d))


def closest_pair(points):
    points.sort(key=lambda p: p[0])
    return closest_util(points)


# Example Usage

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

print(f"Smallest distance is : {closest_pair(points)}")
