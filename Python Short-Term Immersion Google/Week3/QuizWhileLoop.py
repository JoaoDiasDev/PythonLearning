# 2.
# Question 2
# Fill in the blanks so that the print_prime_factors function outputs all prime factors of the number. A prime factor is a decimal number and divides another number without the rest.

from audioop import mul


def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1
    return "Done"


print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

# 3.
# Question 3
# The following code can lead to an infinite loop: Modify the code so that all the numbers can be completed successfully. Note: Use the number 0 as input to run the function and see the result!


def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0 and n != 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

# 4.
# Question 4
# Fill in the empty function to return the sum of all divisors of a number without including a number. A divisor is a number that is divided by another number without the rest.


def sum_divisors(n):
    sum = 0
    div = 1
    while n > div and n != 0:
        if n % div == 0:
            sum += div
        div += 1
    return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114

# 5.
# Question 5
# The multiplication_table function outputs the result of multiplying the passed number by 1 to 5. An additional requirement is that it must be performed with a break statement whose result does not exceed 25. Fill in the blanks to complete the function that satisfies these conditions.


def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
        # What is the additional condition to exit out of the loop?
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24
