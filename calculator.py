import math

def startMenu ():
    print("Choose from following options:")
    print("1. Square root of the number.")
    print("2. Logarithm.")
    print("3. Exponentiation of Euler's number.")


def calculator():
       startMenu()
       inputValue = input("Choose the options [1/2/3]: ", )

       if inputValue == "1":
           sqrt = input("Enter the number (Remember it should be higher than 0!): ")

           if int(sqrt) < 0:
                print("Error: The number is lower than 0!!!")
           else:
                print("result: ", math.sqrt(int(sqrt)))
       elif inputValue == "2":
           argument = input("Enter the argument: ")
           base = input("Enter the base: ")
           print(math.log(int(argument), int(base)))
       elif inputValue == "3":
           exponent = input("Enter the exponent value: ")
           print(math.exp(int(exponent)))
       else:
            print("Choose the right option!!!")
           
   
calculator() 

