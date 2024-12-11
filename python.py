def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if pivot > x]
    right = [x for x in arr[1:] if pivot <= x]

    return quicksort(left) + [pivot] + quicksort(right)


test = [4, 3, 2, 7, 7, 6, 1, 5, 9, 7, 8, 10, 11]

print(quicksort(test))
