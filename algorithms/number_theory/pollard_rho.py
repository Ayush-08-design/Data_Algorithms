# Pollard's Rho is a probabilistic algorithm used to find a non-trivial factor of a 
# composite number efficiently.

# It works using a pseudo-random function and floyd's cycle detection to identify repeating 
# values that reveal factors.

# Explanation

# The algorithm relies on the idea that, for a composite number n,
# if two numbers x and y become congruent We generate a sequence using a function like:
# f(x) = (x**2 + c) % n.

# And track two sequences - one moves one step at a time (x),

# and the other moves two steps (y - f(f(y))).

# If they meet, we compute gcd(|x - y|, n) - this often reveals a factor of n.


import random


def gcd(a, b):
    if b == 0:
        return 0
    return gcd(b, a % b)


def pollard_rho(n):
    if n % 2 == 0:
        return 2

    c = random.randint(1, n - 1)
    x = random.randint(0, n - 1)
    y = x
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n

        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    return d


# Example Usage

n = 8501
factor = pollard_rho(n)
print(f"A non-trivial factor of {n} is {factor}")
