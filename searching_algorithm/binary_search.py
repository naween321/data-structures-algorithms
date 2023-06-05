def binary_search(list1, key):  # binary search example
    low = 0
    high = len(list1) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found:
        print("Key found")
    else:
        print("Key not found")


list1 = [23, 1, 4, 2, 3, 5]
list1.sort()
key = int(input("Enter search value: "))
binary_search(list1, key)
