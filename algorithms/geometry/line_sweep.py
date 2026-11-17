# The line sweep algorithm (or plane sweep algorithm) is an algorithmic technique
# that solves interval and geometric problems by moving an imaginary vertical line
# across a plane.
# Instead of checking every coordinate continuously,
# the algorithm jumps only between discrete points where the state changes,
# reducing the time complexity for most problems to O(n log n).

# Explanation

# Events - We create events for all segment endpoints (left & right)
# Sweep line - Imagine a vertical line moving left to right across the plane
# Active Set - As we move, we maintain all segments that currently intersect the sweep line.
# Intersection check - When a new segment is added, we only need to check it with its
# immediate upper and lower neighbours in the active set

# Result - If any intersection occurs, we record or print it.
# This reduces redundant checks and is far more efficient than comparing all pairs (O(n * n))


import heapq


class Segment:

    def __init__(self, x1, y1, x2, y2):
        if (x1, y1) <= (x2, y2):
            self.x1, self.y1 = x1, y1
            self.x2, self.y2 = x2, y2
        else:
            self.x1, self.y1 = x2, y2
            self.x2, self.y2 = x1, y1

    def get_y(self, x):
        if self.x1 == self.x2:
            return self.y1
        return self.y1 + (self.y2 - self.y1) * (x - self.x1) / (self.x2 - self.x1)


def intersect(s1: Segment, s2: Segment):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if abs(val) < 1e-9:
            return 0
        return 1 if val > 0 else 2

    def on_segment(p, q, r):
        return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[
            1
        ] <= max(p[1], r[1])

    p1, q1 = (s1.x1, s1.y1), (s1.x2, s1.y2)
    p2, q2 = (s2.x1, s2.y1), (s2.x2, s2.y2)

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    # Fixed collinear checks (o1, o2, o3, o4)
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def get_intersection_point(s1: Segment, s2: Segment):
    if not intersect(s1, s2):
        return None

    a1 = s1.y2 - s1.y1
    b1 = s1.x1 - s1.x2
    c1 = a1 * s1.x1 + b1 * s1.y1

    a2 = s2.y2 - s2.y1
    b2 = s2.x1 - s2.x2
    c2 = a2 * s2.x1 + b2 * s2.y1

    determinant = a1 * b2 - a2 * b1

    if abs(determinant) < 1e-9:
        return max(s1.x1, s2.x1), max(s1.y1, s2.y1)

    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return (x, y)


def line_sweep(segments: list[Segment]):
    pq = []
    counter = 0

    for seg in segments:
        heapq.heappush(pq, (seg.x1, seg.y1, 0, counter, seg, None))
        counter += 1
        heapq.heappush(pq, (seg.x2, seg.y2, 2, counter, seg, None))
        counter += 1

    active = []
    intersections = set()
    scheduled_intersections = set()

    def check_and_schedule(s1, s2, current_x):
        if s1 is None or s2 is None:
            return
        pair = tuple(sorted([s1, s2], key=id))
        if pair in intersections:
            return

        pt = get_intersection_point(s1, s2)
        if pt is not None:
            intersections.add(pair)
            ix, iy = pt
            if ix >= current_x - 1e-9 and pair not in scheduled_intersections:
                scheduled_intersections.add(pair)
                nonlocal counter
                heapq.heappush(pq, (ix, iy, 1, counter, s1, s2))
                counter += 1

    while pq:
        x, _y, typ, _, seg1, seg2 = heapq.heappop(pq)

        if typ == 0:
            idx = 0
            while idx < len(active) and active[idx].get_y(x + 1e-7) < seg1.get_y(
                x + 1e-7
            ):
                idx += 1
            active.insert(idx, seg1)

            above = active[idx - 1] if idx > 0 else None
            below = active[idx + 1] if idx < len(active) - 1 else None

            check_and_schedule(above, seg1, x)
            check_and_schedule(seg1, below, x)

        elif typ == 2:
            if seg1 in active:
                idx = active.index(seg1)
                above = active[idx - 1] if idx > 0 else None
                below = active[idx + 1] if idx < len(active) - 1 else None
                active.pop(idx)

                check_and_schedule(above, below, x)

        elif typ == 1:
            if seg1 in active and seg2 in active:
                i1, i2 = active.index(seg1), active.index(seg2)
                if abs(i1 - i2) == 1:
                    active[i1], active[i2] = active[i2], active[i1]
                    low_idx, high_idx = min(i1, i2), max(i1, i2)

                    if low_idx > 0:
                        check_and_schedule(active[low_idx - 1], active[low_idx], x)
                    if high_idx < len(active) - 1:
                        check_and_schedule(active[high_idx], active[high_idx + 1], x)

    return list(intersections)


# Example Usage
segments = [
    Segment(1, 1, 4, 4),
    Segment(1, 4, 4, 1),
    Segment(5, 2, 7, 2),
    Segment(2, 0, 2, 5),
]

result = line_sweep(segments)
print(f"Intersections found ({len(result)}):")
for s1, s2 in result:
    print(
        f"Segment ({s1.x1},{s1.y1})-({s1.x2},{s1.y2}) intersects with"
        f" ({s2.x1},{s2.y1})-({s2.x2},{s2.y2})"
    )
