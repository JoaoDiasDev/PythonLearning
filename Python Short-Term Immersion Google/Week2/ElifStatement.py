# number_group function must return "positive" if the received number is positive, "negative" if it is negative, and "0" if it is 0. Can you fill in the gaps to do so?

def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


print(number_group(10))  # Should be Positive
print(number_group(0))  # Should be Zero
print(number_group(-5))  # Should be Negative
