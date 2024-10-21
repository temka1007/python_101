def square_digits(num):
    square = [int(x)*int(x) for x in str(num)]
    result = "".join(str(x) for x in square)
    return int(result)


print(square_digits(9119))