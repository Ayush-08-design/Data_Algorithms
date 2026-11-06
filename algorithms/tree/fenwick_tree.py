# A Fenwick Tree (also known as Binary Indexed Tree) is a data structure that efficiently
# supports prefix sum queires and updates, on an array in O(log n) time.

# It's an elegent alternative to segment trees for cumulative freequency or prefix sum problems.

# Explanation

# Suppose we have an array of numbers and need to freequently:

# Update a value at an index.
# Find the sum of first k elements.

# A Naive approach (using prefix sums) would take O(n) for updates or queries .
# But a fenwick tree allows both operations in O(log n) using bit manipulation.

# It works by storing cumulative sums in a clever way - each tree node covers a specific
# range of array indices determined by the least sigificant bit (LSB) of the index.

# For an index i:

# Parent Node : i + (i & -i)

# Responsible Range : from (i - (i & -1) + 1) to i


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, value):
        while i <= self.n:
            self.tree[i] += value
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

    def range_sum(self, l, r):
        return self.query(r) - self.query(l - 1)



# Example Usage

array = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2]

n = len(array)

ft = FenwickTree(n)

for i in range(1, n + 1):
    ft.update(i, array[i - 1])

print(f"Prefix sum till index 5 : {ft.query(5)}")

print(f"Sum from index 3 to 7 : {ft.range_sum(3, 7)}")

print("Updating value of index 5 by + 2 .......")

ft.update(5, 2)

print(f"New prefix sum till index 5 : {ft.query(5)}")