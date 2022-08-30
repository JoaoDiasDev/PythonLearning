# Use the get_seconds function to calculate the amount of 2 hours and 30 minutes of seconds, and then add this number to the amount of seconds of 45 minutes and 15 seconds. Then print the results.

def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)
