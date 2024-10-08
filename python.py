array_of_numbers = []

array_index = int(input("Enter number of elements: "))

for i in range(0, array_index):
    ele = int(input("Enter your numbers one by one: "))
    array_of_numbers.append(ele)


def find2max(list):
    array_item_number = len(list)
    if (array_item_number%2) == 0:

        total = array_item_number//2

        first_half = array_of_numbers[total:]
        second_half = array_of_numbers[:total]

        first_half.sort()
        second_half.sort()

        maximum_value_of_first_half = first_half[-1]
        maximum_value_of_second_half = second_half[-1]

        print(f"{maximum_value_of_second_half, maximum_value_of_first_half}")


    else:
        print("Wrong input")

find2max(array_of_numbers)
