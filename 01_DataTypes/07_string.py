#  String "" / ''
my_name = 'Masum'
print(f"My name is {my_name}")

life_update = "Life is Beatiful"
print(life_update)

# life access
# life = life_update[0:4]
# print(f"First text {life}")

print(f"First text {life_update[0:4]}")
# if start from 0 index no need to write as [0:8] write as [:8]
print(f"last text: {life_update[8:]}")

print(f"is text {life_update[5:8]}")

# Starting point : endding point(explicit) : step size
print(f"one after one : {life_update[::2]} ")

# reverse
life_update = "Life is Beatiful" 
print(f"Reverse: {life_update[::-1]}")





