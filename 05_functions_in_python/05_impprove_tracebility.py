def add_vat(price,vat_rate):
    return print(f"Your main price {price} and with vat price is {price+price*(vat_rate/100)}")

orders_price = [100,200,350,150]

for goru in orders_price:
    add_vat(goru,11)
