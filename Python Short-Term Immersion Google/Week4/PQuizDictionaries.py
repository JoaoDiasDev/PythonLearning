# Question 1
# The email_list function receives a dictionary that includes the domain name as the key and contains the list of users as the value. To create a list that contains complete email addresses (for example, diana.prince@gmail.com), fill in the blanks.

def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user+'@'+domain)
    return (emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# Question 2
# The groups_per_user function receives a dictionary containing the group name along with a list of users. A user can belong to multiple groups. Fill in the blanks to return a dictionary that contains the user as the key and the list of their groups as values.

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            user_groups[user].append(group)

    return (user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"]}))

# Question 3
# The dict.update method updates one dictionary with an entry taken from another dictionary, so the existing entry is replaced and a new entry is added. What is the content of the dictionary "wardrobe" at the end of the following code?

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': [
    'yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

# {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
print(wardrobe)


# Question 5
# The add_prices function returns the total price of all the groceries in the dictionary. To finish writing this function, fill in the blanks.

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for items, value in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += value
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44
