# 1.
# Question 1
# Let's test our knowledge of how to use dot notation to access the methods and properties of an object. Let's say you have a class called Birds. Birds have two properties: color and number. Birds also has a method called count() that counts the number of birds (adding a value to the number). Which of the following lines of code correctly outputs the number of birds? The number of birds is 0 until counted!

from itertools import count
from macpath import join


print(bluejay.number.count())

# 2.
# Question 2
# Creating a new instance of a class object can be a good way to track values using properties associated with the object. The values of these properties can be easily changed at the object level. The following code displays a famous quote from George Bernard Shaw that uses objects to represent a person. Fill in the blanks so that your code satisfies the behavior described in the quote.

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw


class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results.
    # We're going to have Martin and Johanna exchange ALL their apples with #one another.
    # Hint: how would you switch values of variables,
    # so that "you" and "me" will exchange ALL their apples with one another?
    # Do you need a temporary variable to store one of the values?
    # You may need more than one line of code to do that, which is OK.
    you_apples = you.apples
    me_apples = me.apples
    me.apples = you_apples
    you.apples = me_apples
    return you.apples, me.apples


def exchange_ideas(you, me):
    # "you" and "me" will share our ideas with one another.
    # What operations need to be performed, so that each object receives
    # the shared number of ideas?
    # Hint: how would you assign the total number of ideas to
    # each idea attribute? Do you need a temporary variable to store
    # the sum of ideas, or can you find another way?
    # Use as many lines of code as you need here.
    you_ideas = you.ideas
    me_ideas = me.ideas
    you.ideas += me_ideas
    me.ideas += you_ideas
    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(
    johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(
    johanna.ideas, martin.ideas))


# 3.
# Question 3
# The City class includes attributes such as Name, Country (where the city is located), Altitude (measured in meters), and Population (approximate based on recent statistics). When comparing the 3 defined instances for a given minimum population, fill in the blanks in the max_elevation_city function to return the city and its country name (separated by commas). For example, if you call a function for a minimum population of 1 million, max_elevation_city (1000000) returns 'Sofia, Bulgaria'.

# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()
    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population >= min_population and city1.elevation > return_city.elevation:
        return_city = city1
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    # Format the return string
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""

# 5.
# Question 5
# There is a brown wooden table and a red leather sofa, two pieces of furniture. Create an instance of each Furniture class and fill in the blanks so that the describe_furniture function creates a statement describing each piece of furniture as follows: "This piece of furniture is made of {color} {material}"


class Furniture:
    color = ""
    material = ""


table = Furniture()
table.color = 'brown'
table.material = 'wood'

couch = Furniture()
couch.color = 'red'
couch.material = 'leather'


def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))


print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"
