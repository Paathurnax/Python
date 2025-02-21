amount = int(input())
day1 = 0
day2 = 0
day3 = 0
day4 = 0
day5 = 0

for i in range(amount):
    personArray = input()
    if personArray[0] == "Y":
        day1 += 1
    if personArray[1] == "Y":
        day2 += 1
    if personArray[2] == "Y":
        day3 += 1
    if personArray[3] == "Y":
        day4 += 1
    if personArray[4] == "Y":
        day5 += 1
  
print(day1, day2, day3, day4, day5)