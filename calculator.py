n = eval(input("Enter your list: ", ))

evenNumbers = [x**2 for x in n if x%2 == 0]

print(evenNumbers)