def grade_result(score):
    if score>=90 and score <=100:
        print(f"Grade  is A+ and Score is {score}")
    elif score>=80 and score <= 89:
        print(f"Grade  is A and Score is {score}")
    elif score >= 70 and score <=79:
        print(f"Grade  is B and Score is {score}")
    elif score >=60 and score <= 69:
        print(f"Grade  is C and Score is {score}")
    elif score <60:
        print(f"Grade  is Fail and Score is {score}")
    else:
        print("Invalid Input")
    

score = int(input("Enter Your Score: "))
grade_result(score)     
