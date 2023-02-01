# def fibonacci():
#     a = 0
#     b = 1
#     while True:
#         c = a
#         a = b
#         b = a + c
#         yield c
#
#
# f = fibonacci()
# for _ in range(20):
#     print(next(f))

# With recursion


def fib(a, b, count):
    print(a)
    c = a + b
    count += 1
    if count == 20:
        return
    return fib(b, c, count)


fib(0, 1, 0)
