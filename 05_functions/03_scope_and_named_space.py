def serve_tea():
    tea_type = 'Masala Tea' # Local Scoe
    print(f"Inside function : {tea_type}")

tea_type = 'Lemom'
serve_tea()
print(f"Outside Function: {tea_type}")

def tea_counter():
    tea_order = 'Lemon' #Enclosing Scope
    def print_order():
        tea_order= 'Gingar'
        print(f"Inner: {tea_order}")
    print(f"Outer: {tea_order}")

tea_order = 'Tulsi' # Global
tea_counter()
print(f"global: {tea_order}")