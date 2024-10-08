chosen_lambda = input("Which lambda function (1, 2, 3): ", )
array_of_numbers = []

array_index = int(input("Enter number of elements: "))

for i in range(0, array_index):
    ele = int(input("Enter your numbers one by one: "))
    array_of_numbers.append(ele)


def modify_list(array, selection):
    lambda_function_1 = lambda x: max(x)
    lambda_function_2 = lambda x: min(x)
    lambda_function_3 = lambda x: 0 in x

    if selection == "1":
        array.append(lambda_function_1(array))
        print(array, "1")
    elif selection == "2":
        array.append(lambda_function_2(array))
        print(array, "2")
    elif selection == "3":
        print(array, lambda_function_3(array))
    

modify_list(array_of_numbers, chosen_lambda)