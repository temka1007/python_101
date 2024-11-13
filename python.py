def create_phone_number(n):
    a = "".join(str(x) for x in n)
    return f"({a[0:3]}) {a[3:6]}-{a[6::]}"

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(create_phone_number(test))