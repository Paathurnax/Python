def multiply(number1, number2):
    '''returns the two numbers multiplied together'''

    product = 0
    for times in range(number2):
        product = product + number1
    return product

answer = multiply(9, 3)
print(answer)
    