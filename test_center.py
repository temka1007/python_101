def frequency_counter(lst):
    def frequency(item, lst):
        total = 0
        for current in lst:
            if item == current:
                total += 1
        return total

    sentence = lst.split(" ")
    new_dict = {item: frequency(item, sentence) for item in sentence}
    return new_dict


test = input("Enter your sentence! ")

print(frequency_counter(test))
