for number in range(1,51): 
    if number %2 == 0:
        print(f"Even Number is:{number}")

number_while = 1
while number_while <= 50:
    if number_while %2==0:
        print(f"Even Number from While is:{number_while}")
    number_while += 1


language = ["Python", "FastAPI", "Docker"] 

for index, item in enumerate(language,start=1):
    print(f"Index {index} value is : {item}")