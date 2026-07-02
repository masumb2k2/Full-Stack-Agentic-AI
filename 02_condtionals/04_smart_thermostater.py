device_status = 'active'
tempreature = int(input("Enter Tempareture: "))

if device_status == 'active':
    if tempreature >=35:
        print("Hot weather")
    else:
        print("Normal Temperature")    

else:
    print("Device Inactive")

