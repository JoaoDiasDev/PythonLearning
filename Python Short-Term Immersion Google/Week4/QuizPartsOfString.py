# Would you like to try it yourself? Do it! Modify the first_and_last function to return true if the first letter of the string is the same as the last character of the string, and false if it is different. Remember that you can use message[0] or message[-1] to access characters. Pay attention to how you handle empty strings. An empty string must return true because it has nothing to compare to.

def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
