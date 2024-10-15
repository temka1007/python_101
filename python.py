isPrime = int(input("Enter your number to check if it is prime number or not: ", ))

for number in range(2, isPrime): 
    value = isPrime/number
    if value.is_integer():
        print("Not prime number!!!")
        break
    elif isPrime == number+1:
        print("Prime number!!!")
        
        