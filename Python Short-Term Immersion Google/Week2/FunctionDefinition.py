# Do you think you can refine a function on its own? I think it can be done! Let's give it a try.

# The hour, minute, and second function parameters specify the body of the print_seconds function to print a given total number of seconds. Remember that 1 hour is 3600 seconds and 1 minute is 60 seconds.

def print_seconds(hours, minutes, seconds):
    print((hours * 3600) + (minutes * 60) + (seconds))


print_seconds(1, 2, 3)
