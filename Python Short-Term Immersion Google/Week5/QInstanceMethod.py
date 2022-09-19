# Now, it's your turn! Take a look at the write methods for the class.

# Based on the Piglet class shown previously, create a Dog class dog_years (1 year for a human being is 7 years for a dog).

class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())
