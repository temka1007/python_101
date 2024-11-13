def digital_root(n):
    number = n
    while len(str(number)) > 1:
        intLst = [int(x) for x in str(number)]
        number = sum(intLst)
    return number

test = 493193

print(digital_root(test))