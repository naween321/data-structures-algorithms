"""
WAP to print duplicates present in the list
"""

data = ["hello", 10, 20, 40, 20, 60, 40, 30]
repeated = []
for i in data:
    if data.count(i) > 1 and i not in repeated:
        repeated.append(i)
print(repeated)