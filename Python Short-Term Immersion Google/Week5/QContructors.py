# Want to see this in action? This code has a Person class with a property name that is set when the object is created. 1) Fill in the spaces so that the properties are set correctly when an instance of the class is created, and 2) when the Greeting() method is called, a greeting indicates the assigned name.

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)


# Create a new instance with a name of your choice
some_person = Person('JoaoDias')
# Call the greeting method
print(some_person.greeting())
