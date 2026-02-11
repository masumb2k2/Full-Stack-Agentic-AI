cup_size = input("Enter Your Cup Size(Small/Medium/Large):").lower()

if cup_size == 'small':
    print("You have to pay 10$")
elif cup_size == 'medium':
    print("You have to pay 15$")
elif cup_size == 'large':
    print("You have to pay 20$")
else:
    print("Unknown cup size")