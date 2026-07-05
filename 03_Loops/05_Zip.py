
customer_name = ['Masum', 'Oishi', 'sabrina', 'Himely', 'Mehtaz']
order_amount = [70,500,100,400,20]

for name,amount in zip(customer_name,order_amount):
    print(f"{name} paid {amount}")