# Remember the Person class from the last video? Let's add a docstring to the greeting method. What about "output a message by person's name"?

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        """Output a message by person's name."""
        print("Hello! My name is {name}.".format(name=self.name))


help(Person.greeting)
