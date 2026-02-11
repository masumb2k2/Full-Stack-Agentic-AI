order_amount = int(input("Enter Your Order Amount: "))


delivery_fee = 0 if order_amount >300 else 30
print(f"Delivery free: {delivery_fee}")
# print(f"Delivery free: {0 if order_amount >300 else 30}")