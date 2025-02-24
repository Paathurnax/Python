og = input()
new = input()
quiet = "-"
letters = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    if i in og and i not in new:
        letters.append(i)
    elif i in new and i not in og:
        replaced = i
        
if len(og) > len(new):
    if new.replace(replaced, letters[0]) == og.replace(letters[1], ""):
        quiet = letters[1]
        silly = letters[0]
    else:
        quiet = letters[0]
        silly = letters[1]
else:
    silly = letters[0]
                   
print(silly, replaced)
print(quiet)
