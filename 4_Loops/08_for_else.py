interviewer = [('masum',24),('sabrina',23),('oishi',22),('mohu',25)]

for name, age in interviewer:
     if age>22:
          print(f"Eligible candidate name is {name} and age is {age}")
          break
else:
    print("No Eligible Candidate here")