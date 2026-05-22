# Dictionary is nothing but key value pair

# name (KEY) = masum (Value)
#  Key & value pair is called as Item
registered_customer = {
    'name': 'john',
    'age': 24,
    'address': 'Dhaka'
}

# Entire dictionary Call
print(f"Registered Customer: {registered_customer}")
# Value Retrive
print(f"Customer Name: {registered_customer['name']}")
# Add new item 
registered_customer['Gender'] = 'Male'
print(f"Registered Customer after add: {registered_customer}")

# update value
registered_customer['age'] = 30
print(f"Registered Customer after update: {registered_customer}")

# delete item 
del registered_customer['address']
print(f"Registered Customer after delete addresss: {registered_customer}")

# membershipm testing
print(f"class existence in customer :{'class' in registered_customer}")

# Only key finding 
print(f"only keys: {registered_customer.keys()}")
print(f"only value: {registered_customer.values()}")
print(f"only items: {registered_customer.items()}")

# pop item 
last_item = registered_customer.popitem()
print(f"Popped item: {last_item}")

# update with another dictionary
another_dictionary ={
    'class' : 13, 
    'dept' : 'CSE'
}

registered_customer.update(another_dictionary)
print(f"Updated Customer List : {registered_customer}")

# Value fetching
# print(f"Customer Name: {registered_customer['university']}")

university_data = registered_customer.get('university', 'Not found')
print(f"Customer Name: {university_data}")


# all customer data
all_customer_data = [
    {'name': 'sabrina', 'age': 24, 'gender': 'Female'},
    {'name': 'Mehtaz', 'age': 30, 'gender': 'Female'},
    {'name': 'oishi', 'age': 28, 'gender': 'Female'},
]
print(f"type of customer data: {type(all_customer_data)}")

print(f"Mehtaz data {all_customer_data[1]}")
mehtaz_data = all_customer_data[1]
print(f"type of mehtaz data: {type(mehtaz_data)}")
mehtaz_name = mehtaz_data.get('name', 'no name')
print(f'Mehtaz name: {mehtaz_name[1:4]}')
print(f"type of mehtaz name: {type(mehtaz_name)}")

# List inside Dictionary
all_customer_history = {
    'name': ['masum','john'],
    'age': [24, 22]
}
all_age = all_customer_history['age']
print(f'All age: {all_age}')

print(f"John age: {all_age[1]}")