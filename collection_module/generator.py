def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Using the generator to generate Fibonacci numbers
fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))  # Output: 0 1 1 2 3 5 8 13 21 34
