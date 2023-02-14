import logging
import employee
logging.basicConfig(level=logging.INFO, filename='test.log', format='%(asctime)s:%(levelname)s:%(message)s')


def add(n1, n2):
    try:
        return n1 + n2
    except TypeError:
        logging.exception("Type Difference")


num1 = 10
num2 = "abc"

add_result = add(num1, num2)
logging.debug(f"{num1} + {num2} = {add_result}")
