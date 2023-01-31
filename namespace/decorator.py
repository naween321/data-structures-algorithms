import time


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print(f'execution time {end-start} seconds')
        return f
    return wrapper


@timed
def calculation():
    for i in range(10000):
        print(i*3)


calculation()
