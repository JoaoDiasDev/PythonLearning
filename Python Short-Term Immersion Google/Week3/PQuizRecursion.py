# Question 3
# Fill in the blanks so that the function can return whether the number is a power of a given base or is_power_of. Note: The base is assumed to be a positive number. Tip: For functions that return fire values, you can return the results of the comparison.

def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        if number == 1:
            return True
        return False

    # Recursive case: keep dividing number by base.
    return is_power_of(number/base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False

# Question 4
# The count_users function recursively counts the number of users in a group in the corporate system through each member of the group, and if one of them is a group, the function is called recursively and counts the number of members. There is a bug! Is it possible to find and fix the problem?


def count_users(group):
    count = 0
    for member in get_members(group):
        count += 1
        if is_group(member):
            count += count_users(member) - 1
    return count


print(count_users("sales"))  # Should be 3
print(count_users("engineering"))  # Should be 8
print(count_users("everyone"))  # Should be 18

# Question 5
# With a recursive function that returns the sum of all positive numbers between the received numbers n and 1, run the sum_positive_numbers function. For example, if n is 3, it must return 1+2+3=6, and if n is 5, it must return 1+2+3+4+5=15.


def sum_positive_numbers(n):
    if n < 1:
        return 0
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15
