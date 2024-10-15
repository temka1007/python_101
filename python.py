
def my_map(func, lst):
    result = []
    for element in lst:
        result.append(func(element))

    return result


numbers = [2, 3, 4, 5, 6, 7, 8, 9]

print(my_map(lambda x: x**2, numbers))