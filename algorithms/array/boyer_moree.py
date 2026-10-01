# The Boyer-Moore Majority Voting Algorithm is an optimal streaming algorithm designed 
# to find the majority element in a sequence—defined as an element that appears strictly 
# more than N/2 times (where N is the size of the array)

# Algorithm
# we maintain a count : 
# if the current element equals the candidate -> increment count . 
# otherwise decrement the count
# at the end the candidate is the potential majority element


## Example Usage

def majority_element(nums):
    candidate , count = None , 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


candidates = [2, 2, 1, 1, 1, 2, 2]
print(f'Candidates array : {candidates}')
print(f'Majority Element : ' , majority_element(candidates))