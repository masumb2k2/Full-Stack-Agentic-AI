# Collection of Unique Element 

# Touple List Set 

shop_item = {"Fried Rice", 'Chicken Fry', 'onthon', 'Tea', 'coffee'}
new_item = {'coffee', 'biriyani', 'hot choclate', 'coffee' }

print(f"New added item: {new_item}")

common_item = shop_item & new_item  # union
print(f"common items: {common_item}")

all_items = shop_item | new_item # intersection
print(f"All item in Two sets : {all_items}")
print(f"All item in Two sets : {type(all_items)}")


# Diffrence 
only_in_shop_item = shop_item - new_item
print(f"only in shop item : {only_in_shop_item}")

# membership testing
print(f"Coffee avalibility in shop item: {'Coffee' in shop_item}")
