def array_diff(a, b):
    return [num for num in a if num not in b]

test_1 = [1,2,2,2,3]
test_2 = [2]

print(array_diff(test_1, test_2))