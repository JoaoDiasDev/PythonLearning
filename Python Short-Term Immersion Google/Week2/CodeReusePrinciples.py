# Ready to try it out for yourself? See if you can reduce code duplication in this script.

# In this code, it identifies the repeating pattern and replaces the name of the month with a function called month_days, which receives the number of days in the month as a parameter. Adjust the rest of the code so that the result is the same. Call the function with the correct parameters for the two months listed to see the results.

# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")

def month_days(month, days):
    print(month + " has " + str(days) + " days.")


month_days("June", 30)
month_days("July", 31)
