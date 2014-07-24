price = input("What is the Price of the Item? ")
tax = input("What is the Sales Tax Percent? ")
tax /= 100.00
print tax
print "The total price of your item is: "+str(price*(1+tax))