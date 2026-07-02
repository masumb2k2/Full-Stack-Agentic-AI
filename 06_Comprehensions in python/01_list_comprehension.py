menu = [
    'Masala Tea',
    'Iced Lemon Tea',
    'Greed Tea',
    'Iced Tea',
    'Gingar Tea'
]

# iced_tea= [tea for tea in menu if 'Iced' in tea]
iced_tea= [tea for tea in menu if len(tea)>10]
print(f"Iced Tea: {iced_tea}")