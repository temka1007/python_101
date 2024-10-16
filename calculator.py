lst = eval(input("List: ", ))

copyLst = lst.copy()

biggest = max(copyLst)

while biggest in copyLst: copyLst.remove(biggest)

print(max(copyLst))