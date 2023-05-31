# [5, 2, 3, 1, 9, 10]
# [[1, 2, 3], [5], [9,10]]


def arrange(lst):
    lst.sort()
    result = []
    group = []
    for i in lst:
        if not group or i-group[-1] == 1:
            group.append(i)
        else:
            result.append(group)
            group = [i]
    else:
        result.append(group)
    return result


print(arrange([5, 2, 3, 1, 9, 10]))
