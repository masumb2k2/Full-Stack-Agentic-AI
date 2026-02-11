device_status = input("Enter Device Status(Active/Inactive):").lower()
temperature = int(input("Enter The Temperature: "))

# print(f"temperature Type: {type(temperature)}")

if device_status =='active':
    if temperature > 35:
        print("High Temperature!")
    else:
        print("Normal Temperature")

else:
    print("Device is Offline")