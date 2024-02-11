import collections


def main():
    Point = collections.namedtuple("P", "x, y")
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1)
    print(p1.x)
    print(p2.y)
    print(type(p1))

    p1 = p1._replace(x=100)


if __name__ == '__main__':
    main()
