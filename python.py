lengthOfList = int(input("how many number supposed to be in here?: ", ))
lst = eval(input("Give your list as follows [a, b, c etc.]: ", ))

if lengthOfList == len(lst)+1:
    for index, element in enumerate(lst, start=1):
        if index != element:
            print(index)
            
else: 
    print("List length is not matching!")

    