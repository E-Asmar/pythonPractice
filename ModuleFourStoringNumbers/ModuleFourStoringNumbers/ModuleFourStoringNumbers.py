#interjecting nubmers into strings
#where % is a place holder
#where d = decimal
print('I have %d cats' % 6) #I have 6 cats where %d brings in the number as a decimal
#%d = Decimal = used for no decimal places
#%f = Float = used for values that contain decimals

print('i have %.2f cats' % 6)
#in {postion in format(list items) zero index : placeholder santion}
print('i have {2:3d} cats'.format(6,9,12,98))

#multi line string
print("here is a string" + \
    " that is on one line but coded in two")
