def add_vat(price,vat_rate):
    return price*(100+vat_rate)/100

orders_AMOUNT =  [100,150,200]

for price in orders_AMOUNT:
    final_amount = add_vat(price,10)
    print(f"Basic amount is {price} and with vat: {final_amount}")