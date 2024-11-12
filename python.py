def spin_words(sentence):
    lst = sentence.split(" ")
    count = 0
    for word in lst:
        if len(word) >= 5:
            print(True)
            lst[count] = lst[count][::-1]
        count += 1
    return " ".join(lst)


test = "Hey fellow warriors"

print(spin_words(test))