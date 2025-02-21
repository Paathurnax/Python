# Gas Mileage Calculator
# Put Your Name Here
# Put the Date Here

# your code goes here
fuel_usage = input("How much gas did you use?")
distance = input("how far did you drive?")

distance = float(distance)
fuel_usage = float(fuel_usage)

mileage = (fuel_usage/distance)
print("you used " + str(mileage*100) + "L per 100km")