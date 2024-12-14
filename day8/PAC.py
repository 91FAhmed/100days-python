import math
def paint_calc(height,width,cover):
    no_of_cans = (height * width) /cover
    print(f"you need {math.ceil(no_of_cans)2} cans")



height = int(input())
width = int(input())
coverage = 5
paint_calc(height=height,width=width,cover=coverage)

