def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        mid_value = arr[middle]

        if mid_value == target:
            return middle
        elif mid_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
