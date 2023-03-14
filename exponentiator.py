def exponentiate(num1, num2) :
    print (num1 ** num2)

def raise_to_fourth_power(num) :
    return exponentiate(num, 4)

#exponentiate(2, 2)

square = lambda num : exponentiate(num, 2)
square(2)

cube = lambda num : exponentiate(num, 3)
cube(2)

raise_to_fourth_power(2)