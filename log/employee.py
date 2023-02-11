import logging
logging.basicConfig(filename='emp.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logging.info(f"Created Employee {self.fullname, self.email}")

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp1 = Employee('John', 'Smith')
emp2 = Employee('Clara', 'Hang')
emp3 = Employee('Jane', 'Doe')
