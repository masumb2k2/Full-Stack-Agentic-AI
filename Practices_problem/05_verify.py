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


# Problem 4 — List
programming_languages = ['Python','C','C++' ,'jave', 'Dart']
print(f"First item is {programming_languages[0]} and last item is {programming_languages[-1]}")
programming_languages.append("Ruby")

programming_languages.pop(1)
print(f"Final List: {programming_languages}")

# Problem 5 — Dictionary
student = {
    'name': 'Masum',
    'age' : 24,
    'gpa' : 3.84,
    'city' : 'Dhaka'
}

for key, value in student.items():
    print(f"key {key}: value {value}")

student['city'] = 'Jhenaidah'
student['graduating'] = True
print(f"Final dictionary: {student}")