# Question 1
# The is_palindrome function checks to see if the string is a loop. A passage reads the same whether it is read from left to right or from right to left, and is a string that leaves spaces and does not use uppercase letters. Examples of passages include words such as kayak and radar and phrases such as 'Never Odd or Even' (not odd or even). Fill in the blanks of this function to return True if the string passed is a loop, otherwise return False.

def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for letter in input_string.lower():
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if letter.replace(" ", ""):
            new_string = letter + new_string
            reverse_string = letter + reverse_string  # Compare the strings
    if new_string[::-1] == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True

# Question 2 - Use the format method to fill in the spaces in the convert_distance function so that Y has only 1 decimal place and returns the syntax 'X miles equals Y km' (X miles equals Ykm). For example, convert_distance 12 must return "12 miles equals 19.2 km" (12 miles equals 19.2 km).


def convert_distance(miles):
    km = miles * 1.6
    result = "{miles} miles equals {km:.1f} km".format(miles=miles, km=km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km

# Question 4
# Use the format method to fill in the spaces in the nametag function so that it returns a period after the first initial of the first_name and last_name. For example, nametag("Jane", "Smith") should return 'Jane S.'


def nametag(first_name, last_name):
    return ("{first_name} {last_name}.".format(first_name=first_name, last_name=last_name[0]))


print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."

# Question 5
# The replace_ending function replaces the old string in the sentence with the new string. However, this is only possible if the sentence ends with the previous string. If a sentence has the previous string more than once, only the string at the end, not the whole, is replaced. For example, replace_ending ("abcabc", "abc", "xyz") returns as abcxyz, not xyzxyz or xyzabc. Because string comparisons are case-sensitive, replace_ending ("abcabc", "ABC", "xyz") must return abcabc (no changes).


def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = sentence.rfind(old)
        new_sentence = sentence[:i]+new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
