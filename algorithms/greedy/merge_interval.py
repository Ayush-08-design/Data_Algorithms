# The interval scheduling or merge intervals algorithm is used to handle problem 
# involving overlapping intervals it helps merge overlapping time ranges or select 
# non-overlapping intervals efficiently by sorting and comparing their start and end time.

# Explanation

# Imagine we have a set of time intervals - like meeting times or class schedules -
# and we want to combine overlapping ones into a single interval

# For example - if we have meetings / intervals: [[1,3],[2,4],[6,8],[7,9]] then the
# merged meetings should be: [[1,4],[6,9]]

# Steps of the algorithm :
# Sort all intervals by their starting time. Initialize a result list with the first interval

# For each subsequent interval:

# If it overlaps with the last merged one -> merge them by updating the end time.
# Else -> add it as a new interval

# The result list will contain all merged intervals.

# This algorithm is often used in calendar apps, cpu scheduling, booking systems,
# and time based data analysis.


def merge_intervals(intervals: list[list[int]]):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged


# Example Usage

intervals = [[1, 3], [2, 4], [6, 8], [7, 9]]

print(f"Original intervals : {intervals}")

merged = merge_intervals(intervals)

print(f"Merged intervals : {merged}")
