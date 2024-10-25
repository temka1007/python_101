def func(param1, param2):
    lst = {char for char in param1 if char in param2}
    return sorted(list(lst))

param = input().split(' ')  

output = func(param[0], param[1])

print(output)