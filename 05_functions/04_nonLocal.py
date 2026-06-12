def update_order():
    tea_type = 'Elachi'
    def kitchen():
        nonlocal tea_type
        tea_type = 'Kesar'
    kitchen()
    print(f"After kitchen update: {tea_type}") 
update_order()