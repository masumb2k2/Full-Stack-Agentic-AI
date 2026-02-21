# def item_list():
#     item_name = 'Soap' # Local Scope
#     print(f"Inside Function: {item_name}")

# item_name = 'Noddles' # Global Scope
# print(f"Outside Function : {item_name}")

# item_list()


def item_list():
    item_name = 'Soap' # Local Scope
    def item_ordered():
        item_name = 'Cake' # Enclosing
        print(f"Inner Function: {item_name}")

    item_ordered()
    print(f"Outer function:{item_name}")


item_list()
item_name = 'Rice' # Global
print(f"Globally : {item_name}")
