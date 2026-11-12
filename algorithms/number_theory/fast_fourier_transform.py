# The Fast Fourier Transform (FFT) is an efficient algorithm to compute the Discrete 
# Fourier Transform (DFT) and its inverse.
# It converts a signal from its time domain to the frequency domain,

# allowing us to analyze frequency components quickly,

# Explanation

# Imagine you have a sound wave (or any signal) represented as a list of sample points,
# The FFT helps us find how much of each frequency is present in that signal - 
# like seprating a musical chord into individual notes.

# The naive DFT algorithm has a time complexity of O(n**2), 
# but FFT, reduces it to O(n log n) by exploiting symmetry and periodicity in complex roots of unity.

# The most commonly used FFT method is the Cooley-Turkey algorithm,
# Which recursively breaks down the problem into smaller sub problems


import cmath


def fft(a: list[int]):
    n = len(a)
    
    if n == 1:
        return a
    
    even = fft(a[0::2])
    odd = fft(a[1::2])
    result = [0] * n

    for k in range(n // 2):
        t = cmath.exp(-2j* cmath.pi * k/n) * odd[k]
        result[k] = even[k] + t
        result[k + n // 2] = even[k] - t
    return result



# Example Usage

arr = [0, 1, 2, 3]
result = fft(arr)

print("FFT output")
for val in result:
    print(val)