class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'  # Developer Readable

    def __str__(self):
        return "Point Object"  # Human Readable


# Original point object
original_point = Point(3, 4)

# Get the string representation of the object
repr_str = repr(original_point)
print(repr_str)  # Output: Point(x=3, y=4)

# Recreate the object using the string representation
recreated_point = eval(repr_str)
print(recreated_point)  # Output: Point(x=3, y=4)
