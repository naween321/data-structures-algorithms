"""
Write a Python program that accepts an integer (n) and computes the value
of n+nn+nnn + …
"""

n = int(input("Enter a number "))
new_n = 0
total = 0
for _ in range(n):
    new_n = new_n * 10 + n
    total += new_n
print(total)
