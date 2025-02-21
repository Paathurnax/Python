def is_odd(some_number):
    '''returns true if the number is odd.
                false if the number is even'''
    if some_number % 2 == 0:
        return False
    else:
        return True
    
def is_even(some_number):
    '''returns true if even.
            return false if odd'''
    return not is_odd(some_number)
    
print(is_even(34))