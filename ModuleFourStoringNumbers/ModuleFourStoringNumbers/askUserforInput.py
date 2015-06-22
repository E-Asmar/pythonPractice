salary = input("Please enter your salary")
bonus = input("please enter your bonus")

#remember 'input()' returns a string
salary = float(salary)
bonus = float(bonus)

paycheckAmount = salary + bonus
#could also write this code as 
# paycheckAmount = float(salary) + float(bonus)

print(paycheckAmount)