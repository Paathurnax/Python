import random

########################################################################################
#Jacob Koshman
#Computer Science 20
#April 12, 2024
#
#Madlibs
#Purpose: To create two madlibs with either user or computer generated input
########################################################################################
print("Answer the second question with only lowercase")
print("----------------------------------------------------------")

#asking the user which madlib they would like to do
madlib_type = input("Which madlib do you want, Old Macdonald or Jack and Gill? ")

#Old Macdonald
if madlib_type == "Old Macdonald":
    
    #asking the user if they want the computer to create the madlib
    computer_madlib = input("Do you want the computer to make the madlib? ")
    if computer_madlib == "yes":
        
        #picking a noun from the text file
        with open("nouns.txt", "r", encoding="UTF-8") as file: 
            nouns = file.read() 
            nouns_words = list(map(str, nouns.split()))

        #picking an adjective from the text file
        with open("adjectives.txt", "r", encoding="UTF-8") as file: 
            adjectives = file.read() 
            adjectives_words = list(map(str, adjectives.split()))

        #picking a name from the text file
        with open("names.txt", "r", encoding="UTF-8") as file: 
            names = file.read() 
            names_words = list(map(str, names.split()))

        #picking an animal from the text file
        with open("animals.txt", "r", encoding="UTF-8") as file:
            animals = file.read()
            animals_words = list(map(str, animals.split()))

        #picking a sound from the textfile
        with open("sounds.txt", "r", encoding="UTF-8") as file:
            sounds = file.read()
            sounds_words = list(map(str, sounds.split()))

        #defining the variables
        adj = str(random.choice(adjectives_words))
        name = str(random.choice(names_words))
        noun = str(random.choice(nouns_words))
        animal = str(random.choice(animals_words))
        sound = str(random.choice(sounds_words))
        
        #printing the madlib
        print("-------------------------------------------------------")
        print(adj + " " + name + " had a " + noun + ", E-I-E-I-O!")
        print("And on his " + noun + " he had a " + animal + ", E-I-E-I-O!")
        print("With a " + sound + "-" + sound + " here and a " + sound + "-" + sound + " there,")
        print("Here a " + sound + ", there a " + sound + ",")
        print("Everywhere a " + sound + "-" + sound)
        print(adj + " " + name + " had a " + noun + ", E-I-E-I-O!")

    #the user makes the madlib
    elif computer_madlib == "no":
        
        #defining the variables
        adj = str(input("Adjective "))
        name = str(input("Name "))
        noun = str(input("Noun "))
        animal = str(input("Animal "))
        sound = str(input("Sound "))
        
        #printing the madlib
        print("-------------------------------------------------------")
        print(adj + " " + name + " had a " + noun + ", E-I-E-I-O!")
        print("And on his " + noun + " he had a " + animal + ", E-I-E-I-O!")
        print("With a " + sound + "-" + sound + " here and a " + sound + "-" + sound + " there,")
        print("Here a " + sound + ", there a " + sound + ",")
        print("Everywhere a " + sound + "-" + sound)
        print(adj + " " + name + " had a " + noun + ", E-I-E-I-O!")
    else:
        print("Try Again")
        
#Jack and Gill
elif madlib_type == "Jack and Gill":
    
    #asking the user if they want the computer to make the madlib
    computer_madlib = input("Do you want the computer to make the madlib? ")
    if computer_madlib == "yes":
        
        #picking a noun from the text file
        with open("nouns2.txt", "r", encoding="UTF-8") as file: 
            nouns = file.read() 
            nouns_words = list(map(str, nouns.split()))

        #picking an item from the text file
        with open("items.txt", "r", encoding="UTF-8") as file: 
            items = file.read() 
            items_words = list(map(str, items.split()))

        #picking a name from the text file
        with open("names.txt", "r", encoding="UTF-8") as file: 
            names = file.read() 
            names_words = list(map(str, names.split()))

        #picking a second name from the text file
        with open("names2.txt", "r", encoding="UTF-8") as file:
            names2 = file.read() 
            names2_words = list(map(str, names2.split()))

        #picking a verb from the text file
        with open("verbs.txt", "r", encoding="UTF-8") as file:
            verbs = file.read()
            verbs_words = list(map(str, verbs.split()))
        
        #picking a thing from the text file
        with open("things.txt", "r", encoding="UTF-8") as file:
            things = file.read()
            things_words = list(map(str, things.split()))
        
        #defining the variables
        item = str(random.choice(items_words))
        name1 = str(random.choice(names_words))
        noun = str(random.choice(nouns_words))
        name2 = str(random.choice(names2_words))
        verb = str(random.choice(verbs_words))
        thing = str(random.choice(things_words))
        
        #printing the madlib
        print("---------------------------------------------------")
        print(name1 + " and " + name2 + " went up the " + noun)
        print("To fetch a pail of " + thing + ";")
        print(name1 + " fell down and broke his " + item)
        print("And " + name2 + " came " + verb + " after.")
    
    #the user makes the madlib
    elif computer_madlib == "no":
        item = str(input("Item "))
        name1 = str(input("Boy Name "))
        noun = str(input("Place "))
        name2 = str(input("Girl Name "))
        verb = str(input("Verb Ending In ing "))
        thing = str(input("Object "))
        
        #printing the madlib
        print("---------------------------------------------------")
        print(name1 + " and " + name2 + " went up the " + noun)
        print("To fetch a pail of " + thing + "s" + ";")
        print(name1 + " fell down and broke his " + item)
        print("And " + name2 + " came " + verb + " after.")
    
    else:
        print("Try Again")
else:
    print("Try Again")
            
