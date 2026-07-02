# Tuple --> ()
coffee_items = ("Black Coffee","latte" ,"Capacino",12)

print(coffee_items)
print(type(coffee_items))
print(type(coffee_items[0]))
first_item = coffee_items[0]
print(first_item)
print(f"Third Item: {coffee_items[2]}")

(first_item, second_item, third_item,fourth_item) = coffee_items
print(f"fourth item {fourth_item}")


print(f"Latee index {coffee_items.index("latte")}")

#SWapo two number
# amm , kola = 1,2
# amm = 10
# kola = 30
# kola, amm = amm, kola
# print(kola)