seat_type = input("Enter your Seat type(Sleeper/Ac/General/Luxury):").lower()

match seat_type:
    case 'sleeper':
        print("Sleeper. Have Sleeping option!")
    case 'ac':
        print("AC. Have Air Conditionar.")
    case 'general':
        print("General. Most Chepest Option")
    case 'luxury':
        print("Luxury. Suite class.")
    case _:
        print("Invalid Seat Type!")