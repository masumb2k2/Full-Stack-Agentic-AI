tea_type = 'plain'

def front_desk():
    def kitchen():
        global tea_type
        tea_type = "Irani"
    kitchen()

front_desk()
print(f"final Global Tea: {tea_type}")