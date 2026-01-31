# Tuples 
shop_items = ("Sugar", "honey", "soap")

print(f"Shop items : {shop_items}")

item1, item2,item3 = shop_items
print(f"Items:{item1},{item2},{item3}")

grocery_item, beauty_item = 1,2
print(f"Items Ratio: G:  {grocery_item} , B:{beauty_item}")

grocery_item, beauty_item = beauty_item, grocery_item
print(f"Items Ratio: G:  {grocery_item} , B:{beauty_item}")

# membership 
print(f"Is Soap in Shop: {"soap" in shop_items}")