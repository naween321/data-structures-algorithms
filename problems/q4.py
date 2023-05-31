"""
frequency of letters in a word
"""

data = "abracadabra"


def solution(s):
    result = dict()
    for i in s:
        try:
            result[i] += 1
        except KeyError:
            result[i] = 1
    return result

print(solution(data))


print(list(zip([1, 2, 3], [4, 5, 6])))
