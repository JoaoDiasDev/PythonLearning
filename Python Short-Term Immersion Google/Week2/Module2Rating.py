# 1.
# Question 1
# Fill in the missing parts to finish writing the function. The color_translator function takes the color name and outputs a hexadecimal value. Since we currently only support 3 additional base colors (red, green, and blue), it returns 'unknown' for all other colors.

def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color


print(color_translator("blue"))  # Should be #0000ff
print(color_translator("yellow"))  # Should be unknown
print(color_translator("red"))  # Should be #ff0000
print(color_translator("black"))  # Should be unknown
print(color_translator("green"))  # Should be #00ff00
print(color_translator(""))  # Should be unknown

# 2.
# Question 2
# What is the value of this Python expression? "big" > "small"

print("big" > "small")
# False

# 4.
# Question 4
# Students in a class receive grades with Pass/Fail. A score of 60 out of 100 or higher means 'Pass'. A lower score than this is 'Fail'. In addition, scores over 95 points (not included) are 'Top Score'. Fill in the function so that the appropriate rating is returned.


def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65))  # Should be Pass
print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
print(exam_grade(95))  # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))  # Should be Fail

# 6.
# Question 6
# format_name completes the creation of the body of the function. This function takes the first_name and last_name parameters, and then returns a well-formed string.

# Specifically:

# If both last_name and first_name parameters are provided, the function should return as follows:

# print(format_name("Ella", "Fitzgerald"))
# Name: Fitzgerald, Ella

# If only one name parameter is provided (first name or last name), the function should return as follows:
# print(format_name("Adele", ""))
# Name: Adele
# or
# print(format_name("", "Einstein"))
# Name: Einstein

# Finally, if both names are empty, the function should return the next empty string.
# print(format_name("", ""))


def format_name(first_name, last_name):
    if (first_name != "" and last_name != ""):
        return ("Name: " + last_name + ", " + first_name)
    elif (first_name != "" or last_name != ""):
        return ("Name: " + first_name + last_name)
    elif (first_name == "" or last_name == ""):
        return ("")


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


# 7.
# Question 7
# Use the longest_word function to compare 3 words: If you need to return the word with the most characters, and the length is the same, use the first in the list. To do this, fill in the blanks.

def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return (word)


print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

# Question 8
# What???s the output of this code?


def sum(x, y):
    return (x+y)


print(sum(sum(1, 2), sum(3, 4)))

# 10.
# Question 10
# The fractional_part function divides the molecule into denominators and returns only the decimal part (a number between 0 and 1). Complete the creation of the body of the function so that it returns the correct number. Note: Dividing by 0 throws an error, so if the denominator is 0, the function should return 0 instead of dividing.


def fractional_part(numerator, denominator):
    if (denominator == 0):
        return 0
    else:
        return (numerator / denominator) % 1


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0
