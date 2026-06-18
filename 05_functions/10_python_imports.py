# import import_test.recipies.flavour
# print(import_test.recipies.flavour.gingar_tea())

# Named import
from import_test.recipies.flavour import gingar_tea,elachi_tea
print(gingar_tea())

# relative Import #
from .import_test.recipies.flavour import gingar_tea,elachi_tea
print(elachi_tea())