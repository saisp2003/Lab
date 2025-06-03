def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        func(*args, **kwargs)
        print("After the function runs")
    return wrapper

# This decorator adds messages before and after the execution of the function.
@my_decorator
def say_hello():
    print("Hello!")
# Demonstrating the decorator functionality by invoking the decorated function
say_hello()
say_hello()

