costprice=float(input("enter your cost price:"))
sellingprice=float(input("enter your selling price:"))
if sellingprice>costprice: 
    print("it is profit")
    profit=sellingprice-costprice
    print("profit is:", profit)
else:    
    print("it is a loss")
    loss=costprice-sellingprice
    print("loss is:",loss)