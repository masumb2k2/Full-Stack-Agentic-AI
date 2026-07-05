# The built-in function in Python adds a counter to an iterable and returns it as an enumerate object

customer_name = ['Masum', 'Oishi', 'sabrina', 'Himely', 'Mehtaz']

for customer_number, name in enumerate(customer_name,start=1):
    print(f"Index {customer_number}: {name}")