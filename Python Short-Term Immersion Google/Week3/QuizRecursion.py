# Question
# The sum_positive_numbers function must return the sum of all positive numbers between the received numbers n and 1. For example, if n is 3, it should return 1+2+3=6, and if n is 5, it should return 1+2+3+4+5=15. To do this, fill in the blanks.

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15
