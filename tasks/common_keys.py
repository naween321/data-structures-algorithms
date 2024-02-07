d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
result = dict()

keys = set(d1.keys()).union(set(d2.keys()))

for key in keys:
    if all([key in d1, key in d2]):
        result[key] = d1[key] + d2[key]
    else:
        result[key] = d1.get(key) or d2.get(key)
print(result)



def one():
    print(two())
    return "fdds"


def two():
    return "dfsd"

print(one())