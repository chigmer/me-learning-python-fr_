#using syntactic sugar

def decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")
    return wrapper
@decorator
def print_stuff():
    print("original function")
print_stuff()