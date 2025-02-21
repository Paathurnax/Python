import random

random_words = 1
if random_words == 1:
    noun = (random.choice(open("nouns.txt","r").readline().split()))
    adj = (random.choice(open("adjectives.txt","r").readline().split()))
    name = (random.choice(open("names.txt","r").readline().split()))
print(str(name) + " has a " + str(adj) + " " + str(noun))
