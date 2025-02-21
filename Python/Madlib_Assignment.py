import random

word_list_noun = ("barn", "house", "chicken")
word_list_adj = ("large ", "crazy ", "tiny ")
word_list_name = (" John", " Bob", " Tim")
noun = (random.choice(word_list_noun))
adj = (random.choice(word_list_adj))
name = (random.choice(word_list_name))
print(str(name) + " has a " + str(adj) + str(noun))
