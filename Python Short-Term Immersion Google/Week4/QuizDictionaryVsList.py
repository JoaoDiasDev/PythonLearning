# In Python, a dictionary can only hold a single value for a given key. To solve this problem, a single value can be a list that contains multiple values. Here is a dictionary called "wardrobe" that contains clothing items and colors. For example, fill in the blanks to print a line for each clothing item with colors like "red shirt", "blue shirt", etc.

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for clothes, colors in wardrobe.items():
    for color in colors:
        print("{} {}".format(color, clothes))
