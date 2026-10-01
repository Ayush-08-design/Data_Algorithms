# Merge Intervals algorithm is an efficient technique used to consolidate a collection 
# of overlapping ranges into a minimal set of mutually exclusive intervals. 
# It is a foundational pattern commonly used in calendar scheduling, resource allocation

# The optimal approach relies on sorting. If the intervals are sorted by their start 
# times, any intervals that can potentially overlap will become adjacent to each other. 
# This reduces the problem from an O(N²) brute-force comparison to a single linear scan.

# Step-by-Step Logic: ------------

# 1. Sort the input array of intervals based on their starting values in ascending order.
# 2. Initialize an empty list (e.g., merged) to hold the consolidated results.
# 3. Iterate through the sorted intervals one by one:
    # • If merged is empty, or if the current interval's start time is greater than the end 
    # time of the last interval in merged, there is no overlap. Append the current interval 
    # directly to merged.
    # • if the current interval's start time is less than or equal to the end time of the last 
    # interval in merged, they overlap. Merge them by updating the end time of the last 
    # interval in merged to be the maximum of its current end time and the current interval's end time
    
    
def maerge_intervals(intervals : list[list[int]]):
    intervals.sort(key = lambda x : x[0])
    merged = [intervals[0]]
    for interval in intervals[1 : ]:
        last = merged[-1]
        if interval[0] < last[1]:
            last[1] = max(last[1] , interval[1])
        else:
            merged.append(interval)
    return merged


## Example Usage ->

intervals = [[1 , 3] , [2 , 6] , [8 , 10] , [15 , 18]]
print(f'Intervals : {intervals}')
print(f'Merged Array of intervals : ' , maerge_intervals(intervals))