order_amount = int(input("Enter Oder Amount: "))

# if order_amount>=300:
#     print("0 tk Delivery chage")
# else:
#     print("delivery charge 30 tk ")

# delivery_charge = 0 if order_amount>=300 else 30
# Ternary Operator
delivery_charge = 'free' if order_amount>=300 else 30
print(f"Delivery Charge is : {delivery_charge}")