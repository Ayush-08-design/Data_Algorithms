# Euler's Totient Function, denoted as Φ(n), counts how many integers from 1 to n are
# coprime to n (i.e., numbers whose greatest common divisor with n is 1).
# In simple words - it tells how many numbers less than or equal to n share no common
# factors with it other than 1.

# Explanation.

# The key property of euler's totient function is:

# if [n = p1^a1 * p2^a2 * .... pk^ak]

# (where p1, p2, .... pk are distinct prime factors of n),

# Φ(n) = n * (1 - 1/p1) * (1 - 1/p2) * .... * (1 - 1/pk)

# For example
# if n = 10 = 2 * 5

# then, Φ(10) = 10 * (1 - 1/2) * (1 - 1/5) = 10 * (1/2) * (4/5) = 4
# So there are 4 numbers (1, 3, 7, 9) that are coprime with 10


def euler_totient(n: int):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


n = 10

print(f"Φ({n}) = {euler_totient(n)}")
