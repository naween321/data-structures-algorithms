def merge_sort(arr):
    length = len(arr)
    if length > 1:
        left_arr = arr[:length//2]
        right_arr = arr[length//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


print(merge_sort([3, 2, 1]))
