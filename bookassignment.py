# 7.5 Create the list
things = ["mozzarella", "cinderella", "salmonella"]

# Capitalizing the element that refers to a person
things[1] = things[1].capitalize()
print("After capitalizing the person:", things)  # Did it change the element? Yes, it modified the list!

# 7.6 Make the cheesy element uppercase
things[0] = things[0].upper()
print("After making the cheesy element uppercase:", things)

# 7.7 Delete the disease element
del things[2]
print("After deleting the disease element (Time to claim that Nobel Prize!):", things)

# 9.1 Define the function 'good' that returns a list of names
def good():
    return ['Harry', 'Ron', 'Hermione']

print("Characters:", good())

# 9.2 Define the generator function 'get_odds' that returns odd numbers from range(10)
def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

# Use a for loop to find and print the third value returned
odds = get_odds()
for i, value in enumerate(odds, start=1):
    if i == 3:  # Find the third odd number
        print("The third odd number is:", value)
        break