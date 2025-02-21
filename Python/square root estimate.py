def my_root(number, guess_amount):
    n = number/2
    for estimate in range(guess_amount):
        n = (1/2)*(n + (number/n))
    return n

thing = my_root(25, 1234)
print(thing)