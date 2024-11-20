
purchase_amount = int(input("'input purchase price of items in ($):"))


if purchase_amount < 100:
 discount = 0
 tax = 0.05 * purchase_amount
 actual_purchase_price = purchase_amount - discount + tax 

elif purchase_amount>= 100 and purchase_amount < 500:
    discount = 0.05 * purchase_amount
    tax = 0.08 * purchase_amount
    actual_purchase_price = purchase_amount - discount + tax

elif purchase_amount >= 500:
    discount = 0.2 * purchase_amount

if discount < 200:
    tax = 0.5 * purchase_amount 
    actual_purchase_price = purchase_amount - discount- tax
    
else: 
    tax = 0.8 * purchase_amount
    actual_purchase_price = purchase_amount - discount- tax
print(f"Your purchase price is ${purchase_amount}")
print(f"Your Discount: ${discount}")
              


    
