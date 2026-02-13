names = ['Masum','Sabrina','oishi','alif','Hosen']
bills = [13,45,50,10,40]

for name,amount in zip(names,bills):
    print(f"{name} paid ${amount}")