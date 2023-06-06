def add(a, b, /, c, d):   # before / are positional only arguments (here a and b)
    return a+b+c+d


print(add(3, 4, c=5, d=6))   # You are not allowed to pass keyword args in the place of positional args


def add(a, b, *, c, d):   # after * are keyword-only arguments (here c and d
    return a+b+c+d


print(add(3, 4, c=5, d=6))  # c and d must be a keyword args
# print(add(3, 4, 5, 6))    This raises an error
