def qwerty_finder(word):
    lst = "qwerty"
    for counter in range(len(word)):
        if word[counter] in lst:
            return counter
    return -1
    
print(qwerty_finder("johnathon"))