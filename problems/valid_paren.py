def is_valid(st):
    opened = ["{", "(", "["]
    closed = ["}", ")", "]"]
    mapping = dict(zip(opened, closed))
    res = []
    for each in st:
        if each in opened:
            res.append(each)
        elif each in closed:
            try:
                close = mapping[res[-1]]
            except IndexError:
                return False
            if not close == each:
                return False
            else:
                try:
                    res.pop()
                except:
                    return False
    return False if res else True


print(is_valid("(]"))
