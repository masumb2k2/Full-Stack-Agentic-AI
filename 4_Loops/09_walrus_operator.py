# Walrus Operator

# value = 11
# remainder = 11%3
# if remainder:
#     print(f"Remainder is {remainder}")
# Using Walrus
# value =11

# if (remainder := value %3):
#     print(f"Remainder is {remainder}")



#task 2
# availabe_tshirt_size =['small','medium','large']

# if (required_size :=input("Enter your Required Size: ").lower()) in availabe_tshirt_size:
#     print(f"Serving size is {required_size}")
# else:
#     print("not availabe")

# task 3

menu_item = ['black','gingar','lemon','green','tulsi']
print(f"Available Item :{menu_item}")

while (required_item := input("Enter your Choice: ").lower()) not in menu_item:
    print("Not availbe")
print(f"Order placed for {required_item}")