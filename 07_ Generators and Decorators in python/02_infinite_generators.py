def infinite_tea():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1
    
refill = infinite_tea()

for _ in range(5):
    print(next(refill))