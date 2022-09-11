# The odd_numbers function returns an odd list between 1 and n. Use the list comprehension to fill in the gaps in the function. Hint: List and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 == 1]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []
