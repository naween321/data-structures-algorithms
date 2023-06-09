# Walrus Operator
# positional only and keyword only
# Named Tuple

from collections import namedtuple

point = namedtuple("Point", "x y")
p = point(1, 2)
print(p.x)
print(p.y)
