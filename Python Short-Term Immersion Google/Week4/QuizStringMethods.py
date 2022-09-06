# Do you want to try some string methods yourself? Give it a try!

# Fill in the spaces in the initials function to return the initials of the words contained in the received phrase in uppercase. For example: "Universal Serial Bus" should return "USB" and "local area network" should return "LAN".

def initials(phrase):
    words = phrase.upper().split()
    result = ""
    for word in words:
        result += word[0]
    return result


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS
