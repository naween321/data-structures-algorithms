def fibonacci():
    a = 0
    b = 1
    while True:
        c = a
        a = b
        b = a + c
        yield c


f = fibonacci()
for _ in range(20):
    print(next(f))
