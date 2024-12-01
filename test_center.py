def count_bits(n):
    remainder = n
    total = []
    while remainder > 0:
        total.insert(0, remainder % 2)
        remainder = remainder // 2
        print(remainder)

    print(total)
    return sum(total)


print(count_bits(16))
