def serve_tea():
    tea_count = 12
    print(f"Local Tea Count is :{tea_count} ")
    def print_count():
        # nonlocal tea_count
        global tea_count
        tea_count = 15
        print(f"Enclosing Tea Count: {tea_count}")
    print_count()

tea_count =5
print(tea_count)
serve_tea()