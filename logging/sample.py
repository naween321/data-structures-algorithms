import logging
logging.basicConfig(level=logging.DEBUG, filename='test.log', format='%(asctime)s:%(levelname)s:%(message)s')


def add(n1, n2):
    return n1 + n2


num1 = 10
num2 = 5

add_result = add(num1, num2)
logging.warning(f"{num1} + {num2} = {add_result}")
