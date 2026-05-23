user_choice = input("Enter Your choice: ").lower()
# print(f"User input: {user_choice}")
# print(f"User input type: {type(user_choice)}")

if user_choice == 'cookies' or user_choice == 'samosa':
    print(f"Order place for: {user_choice}")
else:
    print("Choice Unavailable")
