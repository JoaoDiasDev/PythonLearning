# Now, it's your turn! Repeat the dictionary!

# cool_beasts completes the code that iterates over the keys and values in the dictionary. Remember that the items method returns a tuple of keys, values for each element in the dictionary.

cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for beast, beast_part in cool_beasts.items():
    print("{} have {}".format(beast, beast_part))
