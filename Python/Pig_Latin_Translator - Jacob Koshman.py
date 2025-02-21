##################################################
#Jacob Koshman
#Computer Science 20
#June 12th 2024
#
#Pig Latin Translator
#Purpose: to translate from english to pig latin
##################################################

def reg_translate(text):
    '''translates english text into pig latin'''
    punct = ".,?!"
    vowels = "aeiouy"
    text = text.split()
    for i in range(len(text)):
        letter = text[i]
        if letter[0].isnumeric():
            text[i] = letter
            
        elif letter[0] not in vowels and letter[1] not in vowels and letter[0].isupper() and letter[-1] in punct:
            text[i] = letter[2].capitalize() + letter[3:-1] + letter[:2].lower() + letter[-1]
            
        elif letter[0] not in vowels and letter[1] not in vowels and letter[0].isupper():
            text[i] = letter[2].capitalize() + letter[3:-1] + letter[:2].lower()
        
        elif letter[1] not in vowels and letter[0] not in vowels and letter[-1] in punct:
            text[i] = letter[2:-1] + letter[:2] + "ay" + letter[-1]
            
        elif letter[1] not in vowels and letter[0] not in vowels and letter[-1] not in punct:
            text[i] = letter[2:] + letter[:2] + "ay"
            
        elif letter[0].isupper() and letter[0] not in vowels:
            text[i] = letter[1].capitalize() + letter[2:] + letter[0].lower() + "ay"
            
        elif letter[-1] in punct and letter[0] in vowels:
            text[i] = letter[:-1] + "yay" + letter[-1]
            
        elif letter[-1] in punct and letter[0] not in vowels:
            text[i] = letter[1:-1] + letter[0] + "ay" + letter[-1]
            
        elif letter[-1] not in punct and letter[0] in vowels:
            text[i] = letter + "yay"
            
        elif letter[-1] not in punct:
            text[i] = letter[1:] + letter[0] + "ay"
    
    return " ".join(text)
 
 


print(reg_translate(" "))
            