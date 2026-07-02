def serve_tea():
    yield 'Cup 1: Masala Tea'
    yield 'Cup 2 : Gingar Tea'
    yield 'cup 3: Elachi Tea'

stall = serve_tea()

for cup in stall:
    print(cup)


# Normal function
def get_tea_list():
    return ['cup 1', 'cup 2', 'cup 3']

# Generator function
def get_tea_gen():
    yield 'cup 1'
    yield 'cup 2'
    yield 'cup 3'

tea = get_tea_gen()
print(next(tea))
print(next(tea))
print(next(tea))
# print(next(tea)) # gives error