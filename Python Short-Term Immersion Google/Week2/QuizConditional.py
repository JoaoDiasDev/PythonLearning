# 2.
# Question 2
# Fill in the missing parts to complete the script. This function receives a name and then returns a greeting based on whether the name is 'Taylor' or not.

def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))

# 3.
# Question 3
# If the number is 10, what is the output of this code?

number = 10
if number > 11:
    print(0)
elif number != 10:
    print(1)
elif number >= 20 or number < 12:
    print(2)
else:
    print(3)

#   4.
# Question 4
# Is "A dog" smaller or larger than "A mouse"? Is 9999+8888 less than or greater than 100*100? If you replace the plus sign in the following code, Python can check it and then respond.

print("A dog" > "A mouse")
print(9999+8888 > 100*100)

# Question 5
# If the block size of the file system is 4096 bytes, this means that a file consisting of only 1 byte still uses 4096 bytes of storage. Files that are configured for 4097 bytes use 4096*2=8192 bytes of storage. With that in mind, is it possible to fill in the spaces in the calculate_storage function below that calculate the total number of bytes needed to store a file of a given size?


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0 and full_blocks > 0:
        return block_size * 2
    else:
        return block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192
