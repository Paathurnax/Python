def square(number):
    '''squares the number given by the user'''
    answer = 0
    for times in range(number):
        answer = answer + number
        
    return answer

def sum_to(number):
    '''returns the sum of all numbers from 1 to number'''
    answer = 0
    for times in range(1, (number + 1)):
        answer = answer + times
    return answer

def sum_to_faster(number):
    return (number*(number + 1)) /2

thing = sum_to_faster(10000000000000000000000000000000000000000000000000000)
print(thing)
        
