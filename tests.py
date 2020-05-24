from bot import *

grid = ["rist", "rist", "rist",
        "rist", "rist", "rist",
        False, False, "rist",]


for i in range(100):
    number = main(grid, "rist", "pvb (M)")
    print(number)
