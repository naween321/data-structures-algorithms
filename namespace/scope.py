x = 4

def add():
    y = 3
    x = 5
    summ = x + y
    return summ


print(x)
x = 10
print(add())
globals()['y'] = 100


""" LEGB Local Enclosing Global Built-in scopes """
a = [1, 2, 3]

def test():
    a = [4, 5, 7]
    a.append(8)

test()
print(a)

