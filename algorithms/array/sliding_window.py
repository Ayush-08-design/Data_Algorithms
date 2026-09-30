# sliding window is a technique to process contiguous subarrays / substrings by sliding 
# an window over the input and updating answers in O(1) per move . 
# It turen many brute-force O(n - k) scans to O(n) by reusing work from the previous window. 

# Fixed size window : Window lwngth is constant ( eg - max sum of any k-length subarray).
# Move the right edge one step right and drop the lfetmost element update your running state in O(1).

# Variable sized window : Expand the right edge while a condition holds;
# when it breaks (eg - duplicate appears), shrink from the left until the condition is restored.
# Track the best window during the process.


## Fixed size sliding window (Max sum of any subarray of length k)

def max_sum_k(arr : list[int] , k : int):
    n = len(arr)
    if k <= 0 or k > n:
        return 0 , -1 , -1
    s = 0
    for i in range(k):
        s += arr[i]
    max_sum = s
    bi = 0
    for i in range(k , n):
        s += arr[i]
        s -= arr[i - k]
        s -= arr[i - k]
        if s > max_sum:
            max_sum = bi = i - k + 1
    bj = bi + k - 1
    return max_sum , bi , bj



## Variable sized window : Longest substring without repeting characters

def longest_unique_substring(t):
    position = {}
    l = 0
    mx_len = 0
    bl = 0
    for r , ch in enumerate(t):
        if ch in position and position[ch] >= l:
            l = position[ch] + 1
        position[ch] = r
        curr_len = r - l + 1
        if curr_len > mx_len:
            mx_len = curr_len
            bll = l

    return t[bl : bl + mx_len] , bl , mx_len


# Example Usage
a = [3 ,2 , 7, 1, 8, 3]
k = 3
sum_mx , i , j = max_sum_k(a , k)

s = 'abccabb'
sub , st , ln = longest_unique_substring(s)

print('Max sum K :' , sum_mx)
print('longest unique substring :' , sub)