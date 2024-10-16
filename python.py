lengthOfList = int(input("how many number supposed to be in here?: ", ))
lst = eval(input("Give your list as follows [a, b, c etc.]: ", ))

if lengthOfList == len(lst)-1:
    print("yes")
else: 
    print("no")