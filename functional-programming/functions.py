# functions are first class citizens
# this means that they can be passed as arguments to other functions or returned as the result of other functions
# this also means they can be assigned to variables and used as such

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username}! Welcome the the Python world.")


greet_user('John')

greeting = greet_user
greeting('Peter')

# function composition
def inner():
    print("inner function")


def outer(func):
    func()

outer(inner)


#lambda functions
reverse = lambda s: s[::-1]
print(reverse('hello'))

#reversing a list using a lambda function as the key for the sorted function
cars = ['Ford', 'BMW', 'Volvo']
sorted_cars  = sorted(cars, key=lambda s: -len(s))
print(sorted_cars)

# map function
animals = ['cat', 'dog', 'rabbit']
reverse_animals = list(map(lambda s: s[::-1], animals))
print(reverse_animals)