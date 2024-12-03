def list_merger(a, b):
    lst_1 = a
    lst_2 = b
    merged_list = []
    while len(lst_1) > 0:

        if len(lst_2) == 0:
            break

        while len(lst_2) > 0:

            if len(lst_2) == 0:
                break

            if lst_1[0] > lst_2[0]:
                merged_list.append(lst_2[0])
                lst_2.remove(lst_2[0])
            elif lst_1[0] <= lst_2[0]:
                merged_list.append(lst_1[0])
                lst_1.remove(lst_1[0])
                break

    for item in lst_2:
        merged_list.append(item)
    for item in lst_1:
        merged_list.append(item)

    return merged_list


# MERGE SORT !!!


def merge_sort(lst):
    left_side = lst[: (len(lst) // 2)]
    right_side = lst[(len(lst) // 2) :]

    if len(left_side) > 1:
        left_side = merge_sort(left_side)
    if len(right_side) > 1:
        right_side = merge_sort(right_side)

    return list_merger(left_side, right_side)


test_list = [4, 2, 4, 1, 4, 34, 234, 5, 6, 8, 33, -1, -22, 0, 0.0001]

# SAMPLE RUN !!!

print(merge_sort(test_list))
