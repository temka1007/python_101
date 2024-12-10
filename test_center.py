def subsets_of_set(lst, distance=1):
    if lst == []:
        return lst
    arr = []
    if distance > len(lst):
        return arr
    else:
        print("working")
        for n in range(len(lst) - (distance - 1)):
            arr.append(lst[n : n + distance])
        distance += 1
        return arr + subsets_of_set(lst, distance)


test = ["a", "b", "c"]

print(subsets_of_set(test))
