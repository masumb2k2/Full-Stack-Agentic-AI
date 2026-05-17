# True --> 1  Fasle --> 0

Coffee_item = 5 
is_there_black_coffee = False

total_coffee_count = Coffee_item + is_there_black_coffee  # upcasting
print(f"Total Item {total_coffee_count}")

# 0 & None then only false
is_shop_open = None
# variable = bool(is_shop_open)
print(f"Shop open status : {bool(is_shop_open)}")

# Logical Opertion  --> And Or Not
is_water_boiled = True
is_there_coffee_mix = False

is_serveble = is_water_boiled and is_there_coffee_mix
print(f"Serveble: {is_serveble}")

black_coffee = True
latte_coffe = False

print(f"Coffee order: {latte_coffe or black_coffee} ")

baire_jabi = True
print(f"Baire jabi: { not baire_jabi}")