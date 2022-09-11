# Try the enumeration function yourself in this quick walkthrough. Completes the skip_elements function to return all other elements in the list. This time, we use an enumeration function to check whether an element is in an even or odd position.

def skip_elements(elements):
    elementList = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            elementList.append(element)
    return elementList


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
