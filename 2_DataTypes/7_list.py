shop_items = ['Rice', 'Ice-Cream','Noodles']

#Append
shop_items.append('Cake')
print(f"Shop Items: {shop_items}")

# insert 
shop_items.insert(1,'Potatoo')
print(f"Shop Items: {shop_items}")

# remove list item 
shop_items.remove('Ice-Cream')
print(f"Items afterr remove: {shop_items}")

# remove specific index's item
last_added = shop_items.pop()
print(f"Items after pop : {last_added}")

# 
beauty_item = ['Face-wash','soap']
grocery_item =['Rice','Potatoo']

beauty_item.extend(grocery_item)
print(f"All Item after extend : {beauty_item}")

# reverse
shop_items = ['Rice', 'Ice-Cream','Noodles']
shop_items.reverse()
print(f"Reversed Items: {shop_items}")

# sort 
shop_items.sort()
print(f"sort Items: {shop_items}")

categoriy_wise_item = [12,34,2,35]
print(f"Maximum Item: {max(categoriy_wise_item)}")
print(f"Minium item : {min(categoriy_wise_item)}")

