class Teacup:
    size = 150 # ml
    def describe(self):
        return f"Cup size {self.size} ml"
    
cup = Teacup()
print(cup.describe())

print(Teacup.describe(cup))
cup_2 = Teacup()
cup_2.size = 100
print(Teacup.describe(cup_2))