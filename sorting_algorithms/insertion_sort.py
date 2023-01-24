def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_num = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > cur_num:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                break
    return arr


print(insertion_sort([5, 2, 10, 3, 20, 1]))
