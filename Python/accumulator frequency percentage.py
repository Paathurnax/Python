import requests

def frequency_seen(the_text, letter_find):
    '''counts the frequency of a specific letter in a given text in percentage'''
    
    letter_seen = 0
    the_text = the_text.lower()
    total_letters = 0
    
    for letter in the_text:
        if letter in alphabet:
            total_letters += 1
            if letter == letter_find:
                letter_seen += 1
 
    percentage = (letter_seen/total_letters)*100
    percentage = round(percentage, 2)
    print(f"{letter_find} - {percentage}%")


the_url = "https://www.gutenberg.org/cache/epub/84/pg84.txt"
book = str(requests.get(the_url).content)

alphabet = "abcdefghijklmnopqrstuvwxyz"
for some_letter in alphabet:
    frequency_seen(book, some_letter)