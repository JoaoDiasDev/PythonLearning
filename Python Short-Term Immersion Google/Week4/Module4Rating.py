# Question 1
# The format_address function separates part of the address string into new strings, house_number and street_name, and returns it as 'house number X on street named Y'. The format of the input string is as follows: A numeric street number, followed by a street name, which can contain numbers, but cannot be used alone and can lead to multiple words. For example, "123 Main Street," "1001 1st Ave," or "55 North Center Drive." To finish writing this function, fill in the blanks.

def format_address(address_string):
  # Declare variables
    street_number = ""
    street_name = ""
  # Separate the address string into parts
    address_string = address_string.split(" ")
  # Traverse through the address parts
    for address in address_string:
        # Determine if the address part is the
        # house number or part of the street name
        if address.isnumeric():
            street_number += address
        else:
            street_name += " " + address
  # Does anything else need to be done
  # before returning the result?
  # Return the formatted string
    return "house number {} on street named {}".format(street_number, street_name.strip())


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

# Question 2
# highlight_word function changes a given word in a sentence to an uppercase version. For example, highlight_word ("Have a nice day", "nice") returns "Have a NICE day". Is it possible to write this function on just one line?


def highlight_word(sentence, word):
    return (sentence.replace(word, word.upper()))


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# Question 3
# A professor with two assistants, Jamie and Drew, wants an attendance list that students fill out in the order in which they arrive in the classroom. Drew was the first to write the students who arrived, followed by Jamie. After class, they each entered their own list into a computer and emailed it to the professor, who wants to make the list one in the order in which each student arrived. Jamie, meanwhile, soon emailed her that her list was in reverse order. Follow the steps to combine them into one list as follows: Take the contents of the Drew list and the reverse list of Jamie that follows and make an accurate list of the students in the order in which they arrived.


def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
    new_list = list2 + list1[::-1]
    return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

# Question 4
# Use list comprehension to create a list of squared numbers (n*n). This function takes the variables start and end and returns a  list of consecutive numeric squares all the way between start and end. For example, squares(2, 3) returns [4, 9].


def squares(start, end):
    return [i*i for i in range(start, end + 1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Question 5
# car_prices completes the code that iterates over the keys and values in the dictionary and outputs information about each.


def car_listing(car_prices):
    result = ""
    for car, price in car_prices.items():
        result += "{} costs {} dollars".format(car, price) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
      "Ford Fiesta": 13000, "Toyota Prius": 24000}))

# Question 6
# Taylor and Rory are about to throw a party. They sent out invitations, and each of them collected answers in a dictionary that included the name of each friend and the number of guests each friend would bring. Each dictionary is a partial list, but Rory's list has the latest information on the number of guests. To sum the two dictionaries together, fill in the blanks. If the name is included in both dictionaries, each friend is listed only once, and the number of guests in Rory's dictionary takes precedence. It then prints the dictionary result.


def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    combined_guests = {**guests1, **guests2}
    for key, value in combined_guests.items():
        if key in guests1 and key in guests2:
            combined_guests[key] = guests1[key]
    return combined_guests


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1,
                "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1,
                  "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Question 7
# Use a dictionary to calculate the character frequency of the input string. You should only count characters that are not spaces, numbers, or punctuation. Uppercase letters should be considered the same as lowercase letters. For example, count_letters ("This is a sentence." (This is a sentence.)) returns as follows: {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.


def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text.lower():
        # Check if the letter needs to be counted or not
        letter = letter
        if letter.isalpha():
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
            # Add or increment the value in the dictionary
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


# Question 8
# When animal = "Hippopotamus", what does the following command return:

animal = 'Hippopotamus'

print(animal[3:6])
print(animal[-5])
print(animal[10:])
# pop
# t
# us

# Question 9
# What is included in the "colors" list after this command is executed?

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

print(colors)
# ['red', 'white', 'yellow', 'blue']

# Question 10
# What does the following command return:

host_addresses = {"router": "192.168.1.1",
                  "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()

print(host_addresses.keys())
# ['router', 'localhost', 'google']
