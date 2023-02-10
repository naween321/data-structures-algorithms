x = 4

def add():
    y = 3
    x = 5
    summ = x + y
    return summ


print(x)
print(add())
globals()['y'] = 100
print(globals())
