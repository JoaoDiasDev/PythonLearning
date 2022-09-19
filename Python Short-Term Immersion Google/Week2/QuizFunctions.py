# Question 1
# This function converts miles to kilometers.

# Complete the function creation and return the conversion result.

# Call a function that converts the distance traveled from miles to kilometers.

# To output the conversion result, fill in the blanks.

# Multiply the result by 2 times to calculate the round-trip distance in kilometers, fill in the blanks to print the results.

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = (miles * 1.6)  # approximately 1.6 km in 1 mile
    return km


my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km * 2))

# Question 2
# This function compares two numbers and returns them in ascending order.

# Fill in the blanks so that the print statement displays the results of the function call in order.

# Hint: If your function returns multiple values, remember that you must store these values as multiple variables.

# This function compares two numbers and returns them
# in increasing order.


def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

# 4. Let's look at the lucky_number function again. Instead of outputting a message, you want to change it to return a message. In this way, the calling line can output a message, or it can do it differently if necessary. Fill in the blanks to finish writing the code.


def lucky_number(name):
    number = len(name) * 9
    msg = "Hello " + name + ". Your lucky number is " + str(number)
    return msg


print(lucky_number("Kay"))
print(lucky_number("Cameron"))
