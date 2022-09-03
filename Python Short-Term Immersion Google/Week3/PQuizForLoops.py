# Question 2
# Fill in the blanks to create a factorial function that returns a factorial value n. Then print the first 10 factorial values (from 0 to 9) with that number. Note that factorial numbers are defined as the product of integers, and all integers precede them. For example, the succession of 5 (5!) is equal to 1*2*3*4*5=120. Also the succession of zero(0!) Recall that is equal to 1.

def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result


for n in range(0, 10):
    print(n, factorial(n+1))


# Question 3
# Write a script that outputs the first ten cubic numbers (x**3) starting at x=1 and ending with x=10.

for x in range(1, 11):
    print(x**3)

# Question 4
# Write a script that outputs a multiple of 7 between 0 and 100. Output one multiple per line and not a number that is not a multiple of 7. 0 is also a multiple of 7.

for x in range(0, 100):
    if x % 7 == 0:
        print(x)

# Question 5
# The retry function attempts to execute a task that might fail, and retries the operation several times. Even if the current code succeeds, the function continues to run. After the operation is successful, fill in the blanks so that the code stops trying.


def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break
        else:
            print("Attempt " + str(n) + " failed")


retry(create_user, 3)
retry(stop_service, 5)
