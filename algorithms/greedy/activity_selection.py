# The Activity Selection Problem is a classic combinatorial optimization problem that
# aims to schedule the maximum number of non-overlapping activities

# solved using a Greedy Algorithm, which makes a locally optimal choice at each stage
# with the intent of finding a globally optimal solution.

# Explanation

# 1. Sort all given activities in ascending order based on their finish times.
# 2. Select the first activity from the sorted list, as it finishes earliest.
# 3. Iterate through the remaining activities. For each activity, compare its start time
# to the finish time of the last selected activity.
# 4. Accept the activity if its start time is greater than or equal to the last selected
# activity's finish time. Update your tracking to this new activity's finish time.
# 5. Ignore the activity if it overlaps (starts before the last selected one finishes


def activity_selection(start: list[int], end: list[int]):
    activities = list(zip(start, end))

    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_finished_time = activities[0][1]

    for idx in range(1, len(activities)):
        if last_finished_time <= activities[idx][0]:
            selected.append(activities[idx])
            last_finished_time = activities[idx][1]
        else:
            continue

    return selected



# Example Usage

start  = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

result = activity_selection(start, finish)

print(f"Selected Activities (Start, Finish): {result}")