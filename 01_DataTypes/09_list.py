# list --> []

coffee_items = ["Black Coffee","latte","Capacino" ,"latte",12]

print(f"Type : {type(coffee_items)}")
print(f"items{coffee_items}")

# Add new item on last
coffee_items.append("Cold Coffee")
print(f"After Append items:{coffee_items}")

# Add in specific index
coffee_items.insert(2,'Raw Coffee')
print(f"After insert items:{coffee_items}")

# Remove 
coffee_items.remove("latte")
print(f"After Remove items:{coffee_items}")

# remove specific location
removed = coffee_items.pop()
print(f"After POp items:{coffee_items}")
print(f"Removed item : {removed}")


batch_16 =["Karim", "rahim"]
extra_student = ['Bob', "dolly", "Alex"]

batch_16.extend(extra_student)

print(batch_16)

batch_16.reverse()
print(f"Reverse: {batch_16}")

batch_16.sort()
print(f"Sort: {batch_16}")

# Can find min max when list type is int or number 
# min(listName)