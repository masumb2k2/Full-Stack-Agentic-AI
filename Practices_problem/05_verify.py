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
else:
    print(f"{number} is Zero")


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

# Problem 6 — Tuple & Set
countries = ('Bangladesh', 'India' , 'Japaan', 'China')
# countries[1] = 'USA'
# TypeError: 'tuple' object does not support item assignment
# show this error because touple is immutable data type, user dont can change it's value after assign once

my_favorite_language = {'Python', 'Dart', 'Java'}
friend_favorite_language = {'PHP', 'Python', 'Java'}
print(f"Common languages in both: {my_favorite_language & friend_favorite_language}")

# Problem 7 — Function
def student_result (name, marks):
    if len(marks) != 3:
        print("value Error")
    else:
        average_mark = sum(marks) / len(marks)
        if average_mark >= 50:
            print(f"{name} passed with average {average_mark}")
        else:
            print(f"{name} failed with average {average_mark}")
        
        
student_result('Masum', [88,94,77])
student_result('Mohua', [40,60,35])
