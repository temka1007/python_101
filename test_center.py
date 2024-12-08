def kth_finder(kth, lst):
    sortedLst = sorted(lst)
    print(sortedLst)
    if kth > len(lst):
        return "Given index is larger than list length"
    else:
        return sortedLst[kth - 1]


arr = [7, 10, 4, 3, 20, 15]
print(kth_finder(8, arr))
