def binary_search(arr, val):
    min = 0
    max = len(arr) - 1
    while True:
        if max < min:
            return -1
        mid = (min + max) // 2
        if arr[mid] < val:
            min = mid + 1
        elif arr[mid] > val:
            max = mid - 1
        else:
            return mid