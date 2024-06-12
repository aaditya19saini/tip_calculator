print("Welcome to the Tip Calculator!")

#input from user
amount=int(input("enter the bill amount: \n$:"))
tip=int(input("entre the tip\npercentage: "))
p=int(input("enter the number of people: "))

#float formatting example
total=("{:.2f}".format(((amount*(tip/100))+amount) /p))



# total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))



print("total tip amount is:",total)


    