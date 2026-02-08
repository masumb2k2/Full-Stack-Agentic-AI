beauty_item = ['Face-wash','soap']
grocery_item =['Rice','potatoo']

total_item = beauty_item + grocery_item
print(f"Total Shop item : {total_item}")

extra = grocery_item * 5
print(f"Extra Grocery: {extra}")

# Byte Array
raw_item = bytearray(b'ICECREAM')
raw_item = raw_item.replace(b'ICE',b'HOT')
print(f"Bytearray : {raw_item}")