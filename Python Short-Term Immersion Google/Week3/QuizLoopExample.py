# Question
# In mathematics, the factorial of a number is defined as the product of an integer and all integers below it. For example, the succession of 4 (4!) is equal to 1*2*3*4=24. Fill in the blanks so that the factorial function returns the correct number.

def factorial(n):
    result = 1
    for i in range(1, n):
        result += result * i
    return result


print(factorial(4))  # should return 24
print(factorial(5))  # should return 120
