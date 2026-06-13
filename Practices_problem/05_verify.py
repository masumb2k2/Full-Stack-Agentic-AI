# Problem 1 — Variables & Strings
name = 'Masum'
age = 24
city = 'Dhaka'
print(f"My name is {name}, age {age}, from {city}")
print(f"Name in uppercase : {name.upper()}")
print(f"Number of character in name is: {len(name)}")

# Problem 2 — Conditions
number = int(input("Enter a number: "))
if number>0:
    print(f"{number} is Positive Number")
elif number<0:
    print(f"{number} is Negative Number")
elif number == 0:
    print(f"{number} is Zero")
else:
    print(f"{number} is invalid")

# Problem 3 — Loops
for number in range(1,11):
    print(f"7 X {number} = {7*number}")
