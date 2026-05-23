user_choice = input("Enter your Choice from  small/medium/ large: ").lower()

if user_choice == 'small':
    print(f"You order {user_choice} and price is 10")
elif user_choice == 'medium':
    print(f"You order {user_choice} and price is 15")
elif user_choice == 'large':
    print(f"You order {user_choice} and price is 20")
else:
    print("choice unvailable")

