def fibonacci(a, b, count=0):
    print(a, end="\t")
    c = a + b
    count += 1
    if count == 10:
        return
    return fibonacci(b, c, count)


fibonacci(0, 1)
