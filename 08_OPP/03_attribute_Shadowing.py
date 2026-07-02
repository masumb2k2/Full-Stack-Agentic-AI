class Tea:
    temperature = 'hot'
    strength = 'strong'


cutting_tea = Tea()

print(cutting_tea.temperature)

cutting_tea.temperature = 'mild'
print(f"After Changing: {cutting_tea.temperature}")
print(f"direct look on class: {Tea.temperature}")

del cutting_tea.temperature
print(cutting_tea.temperature)