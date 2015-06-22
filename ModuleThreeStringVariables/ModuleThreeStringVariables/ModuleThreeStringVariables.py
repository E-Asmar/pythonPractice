#takes an input and makes it a variable
name = input("What is your name? ")
print(name)

name = 'CEBOT'
print(name)

#rules for python variables
# 1. cannot contain spaces
# 2. Is case-sensitive 
# 3. cannot start with a number.
# 4. discriptive naming

message = "Hello World"
print(message.lower())
print(message.upper())
print(message.swapcase())

name = input("who are you ? ")
plotDevice = input("give me your thing")
movement = input("how do you move")

print("\nHello " + name + " welcome to Narrth, you have a " + plotDevice.upper() + " and you " + movement + " everywhere.")
