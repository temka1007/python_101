def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    midpoint_index = (left + right) // 2

    if arr[midpoint_index] == target:
        return midpoint_index
    elif arr[midpoint_index] < target:
        return binary_search_recursive(arr, target, midpoint_index + 1, right)
    else:
        return binary_search_recursive(arr, target, left, midpoint_index - 1)


arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 14
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Index of {target}: {result}")
