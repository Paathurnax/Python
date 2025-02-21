#getting data
name = input("What's your name?")
favorite_class = input("What's your favorite class?")
current_year = input("What year is it")
grad_year = input("what year do you graduate?")

#converting data
grad_year = int(grad_year)
current_year = int(current_year)

#do the math
years_until_grad = grad_year - current_year

#print the results
print(name + " will graduate in  " + str(years_until_grad) + " years")