scores = int(input())

all_scores = []
for i in range(scores):
    all_scores.append(int(input()))
    
    
all_scores.sort();

gold = all_scores[-1]
gold_count = (all_scores.count(gold))

index = -1
while True:
    if all_scores[index] != gold:
        silver = all_scores[index]
        break
    else:
        index -= 1
        
silver_index = index

while True:
    if all_scores[index] != silver:
        bronze = all_scores[index]
        break
    else:
        index -= 1
bronze_count = all_scores.count(bronze)
print(f"{bronze} {bronze_count}")