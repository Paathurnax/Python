scores = int(input())
scoreList = []
counter = 0

for i in range(scores):
    scoreList.append(int(input()))
    
gold = max(scoreList)
for i in range(scores):
    if scoreList[i] == gold:
        scoreList[i] = -1
        
silver = max(scoreList)
for i in range(scores):
    if scoreList[i] == silver:
        scoreList[i] = -1
        
bronze = max(scoreList)
for i in range(scores):
    if scoreList[i] == bronze:
        counter+=1

print(bronze, counter)      