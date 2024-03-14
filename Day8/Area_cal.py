import math


def paint_to_buy (height, width, cover):
    area = height*width
    cans=math.ceil(area/cover)
    print(f"You need {cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage  = 5.0
paint_to_buy(height=test_h, width=test_w, cover=coverage)