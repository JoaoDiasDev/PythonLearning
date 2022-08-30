# This function, which calculates the area of a rectangle, has poor readability. Can I call a function that refactored and then calculates an area with a base of 5 and a height of 6?

# Tip: The function that calculates the area of a rectangle should probably be called rectangle_area, and if it receives the base and height, it should call the parameter.

def rectangle_area(base, height):
    area = base*height  # the area is base*height
    print("The area is " + str(area))


rectangle_area(5, 6)
