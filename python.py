def list_merger(a, b):
    lst_1 = a
    lst_2 = b
    merged_list = []
    while len(lst_2) > 0:
        if len(lst_2) == 0:
            merged_list.append(lst_2[0])
            lst_2.remove(lst_2[0])
            break

        print("!!!", merged_list)
        while len(lst_2) > 0:
            if lst_1[0] > lst_2[0]:
                print(lst_1[0], lst_2[0])
                merged_list.append(lst_2[0])
                lst_2.remove(lst_2[0])
                print(lst_2)
            else:
                merged_list.append(lst_1[0])
                lst_1.remove(lst_1[0])
                break

    print(merged_list)


arr1 = [4, 5, 6]
arr2 = [1, 2, 7]

list_merger(arr1, arr2)


def merge_sort(lst):
    if len(lst) > 1:
        pass
    else:
        return lst


test_list = [2, 3, 5, 1, 6, 7, 9, 0]
