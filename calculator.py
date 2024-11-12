def circular(n):
    circuling = []
    for i in range(len(n)):
        rotated = int(n[i:] + n[:i])
        circuling.append(rotated)
    return circuling

def prime(n):
    number = int(n)
    for i in range(2, number): 
        if number%i == 0: 
            return False 
    return True

def circular_prime(n):
    rotations = circular(n)
    return all(prime(rotation) for rotation in rotations)

inputNumber = input()

print(circular(inputNumber))
print(prime(inputNumber))
print(circular_prime(inputNumber))