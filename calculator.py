targetSum = int(input("Target sum: ", ))
lst = eval(input("List: ", ))

counter = 0

for number in lst:
    for innerNumber in lst:
        total = number + innerNumber
        if total == 10:
            lst.remove(number)
            lst.remove(innerNumber)
            counter += 1

print(counter)