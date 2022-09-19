# Question 1
# Fill in the blanks in this code to print out the numbers from 1 to 7.

number = 1
while number <= 7:
    print(number, end=" ")
    number += 1


# Question 2
# The show_letters function prints each character of a word on a separate line. To do so, fill in the blanks.

def show_letters(word):
    for letter in word:
        print(letter)


show_letters("Hello")
# Should print one line per letter

# Question 3
# Complete the function number (n) that returns the number of digits of the number. Example: 25 has 2 digits, and 144 has 3 digits. Tip: You can find out the number of digits by dividing it by 10 once in a single digit until there is not a single number left.

# def digits(n):
# 	count = 0
# 	if n == 0:
#         count = 1
#     while (n >= 10):
# 		count += 1
# 		___
# 	return count


def digits(n):
    count = 0
    if n == 0:
        count = 1
    while (n >= 1):
        count += 1
        n = n // 10
    return count


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))    # Should print 1

# Question 4
# This function outputs the phrase (where each number is the result of multiplying the first number in the row by the number at the top of the column). Fill in the blanks so that the multiplication_table(1, 3) call can output the following: 1 2 3 2 4 6 3 6 9


def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x*y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above

# Question 5
# The counter function counts down from start to stop if the start is greater than the stop, otherwise counts up from start to stop. Fill in the blanks for this feature to work correctly.


def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x = x - 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x = x + 1
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"

# Question 6
# The even_numbers function returns all positively separated strings with spaces divisible by 2, including the maximum value passed to the function. For example, even_numbers(6) returns "2 4 6". To do this, fill in the blanks.


def even_numbers(maximum):
    return_string = ""
    for x in range(maximum):
        x = x + 1
        if x % 2 == 0 and x != 0:
            return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10))  # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

# Question 7
# The following code raises an error when executed. What's the reason for the error?


def decade_counter():
    while year < 50:
        year += 10
    return year

# R: Failure to initialize variables

# Question 8
# What is the value of x at the end of the following code?


for x in range(1, 10, 3):
    print(x)

#R: 7

#     9.
# Question 9
# What is the value of y at the end of the following code?

for x in range(10):
    for y in range(x):
        print(y)

#R: 8

# 10.
# Question 10
# How does this function need to be called to print yes, no, and maybe as possible options to vote for?


def votes(params):
    for vote in params:
        print("Possible option:" + vote)


# R: votes(['yes','no','maybe'])
