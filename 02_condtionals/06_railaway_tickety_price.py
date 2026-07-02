user_choice = input("Enter from AC/ Luxury/ NON Ac/ Sleeper: ").lower()

match user_choice:
    case 'ac':
        print(f"You choose {user_choice}")
    case 'luxury':
        print(f"You choose {user_choice}")
    case 'non ac':
        print(f"You choose {user_choice}")
    case 'sleeper':
        print(f"You choose {user_choice}")
    case _: # Default case
        print("invalid choice")
