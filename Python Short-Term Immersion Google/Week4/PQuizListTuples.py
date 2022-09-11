# Question 1
# With a list of file names, I want to rename all filenames with the extension hpp to extension h. To do this, we want to generate a new list named newfilenames consisting of the new file names. Use the methods you've learned so far, such as for loops or list comprehensions, to fill in the blanks in your code.

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for fname in filenames:
    if fname.endswith(".hpp"):
        fname = fname.replace(".hpp", ".h")
    newfilenames.append(fname)
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# Question 2
# Let's create a function that changes the text to pyglatin. It simply converts the text by moving the first letter of each word to the end and appending 'ay' to the end to modify it. For example, python would be ythonpay.

def pig_latin(text):
    say = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        word = word[1:] + word[0] + "ay"
        # Turn the list back into a phrase
        say.append(word)
    return " ".join(say)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))

# Question 3.
# On Linux systems, the permissions of a file are divided into three sets: read, write, and execute for the owner, group, and other three permissions. Each of the three values can be expressed as a hexadecimal sum of each permission, with 4 being read, 2 being write, and 1 being executing. Alternatively, if no permissions are granted, they can be written as strings using the r, w, x, or - characters. Example: 640 means read/write to the owner, read to the group, and no permissions to anyone else. If you convert it to a string, it's like 'rw-r-----'.

# 755 is read/write/execute for the owner and read/execute for the group and others. If you convert it to a string, it's 'rwxr-xr-x'. Fill in the blanks so that your code converts permissions from hexadecimal to string format.


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

# Question 5
# The group_list function accepts a group name and a member list and returns a string in the following format: group_name: member1, member2, ... For example, group_list ("g", ["a","b","c"]) returns 'g: a, b, c'. Fill in the blanks to execute it in that function.


def group_list(group, users):
    members = ", ".join(users)
    return "{}: {}".format(group, members)


# Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
# Should be "Engineering: Kim, Jay, Tom"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
print(group_list("Users", ""))  # Should be "Users:"

# Question 6
# The guest_list function reads a list of tuples containing the name, age, and occupation of each guest who comes to the party and sets each one to 'Guest is X years and works as __.' (The guest is X years old and the occupation is __.) to output the sentence: For example, guest_list ('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) would output something like this: Ken is 30 years old and works as Chef. (Ken is 30 years old and his job is as a chef.) Pat is 35 years old and works as Lawyer. (Pat is 35 years old and has a professional job as a lawyer.) Amanda is 25 years old and works as Engineer. (Amanda is 25 years old and works as an engineer.) Fill in the blanks to execute it in that function.


def guest_list(guests):
    for guest in guests:
        guest_name, guest_age, guest_occupation = guest
        print("{} is {} years old and works as {}".format(
            guest_name, guest_age, guest_occupation))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
           ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
