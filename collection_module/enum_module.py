from enum import Enum, unique


@unique  # restricts the values to be duplicate.
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3

# Duplicate keys are not allowed by default


print(Fruit.APPLE.value)

