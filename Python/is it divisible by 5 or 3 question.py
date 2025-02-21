number = int(input("What is the number "))

if int(number) % 5 == 0 or int(number) % 3 == 0:
    print("That number is divisible by 5 or 3")
else:
    print("that number is not divisible by 3 or 5")