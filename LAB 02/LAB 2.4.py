#1201200654
#Kong Zi Yin

banana = 1.5
grapes = 5.60

print("Invoice for Fruit Purchase")
print("\n--------------------------\n")
qty = float(input("Enter the quantity (comb) of banana bought : "))
amt = float(input("Enter the amount (kg) of grapes bought : "))

total1 = banana * qty
total2 = grapes * amt
g_total = total1+total2

print("\nItem \t\t\t Qty \t\tPrice \t\tTotal")
print("Banana (combs)\t\t {:.0f} \t\tRM {:.2f} \t RM {:.2f}" .format(qty,banana,total1))

#print("Banana (combs)\t\t ",qty, "\t\tRM " , banana , "\t RM " , total1)

print("Grapes (kg)\t\t {:.0f} \t\tRM {:.2f} \t RM {:.2f}" .format(amt,grapes,total2))
print("\n Total : {:.2f} " .format(g_total))