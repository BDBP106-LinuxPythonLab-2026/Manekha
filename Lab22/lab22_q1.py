def greet_decorator(func):
    def wrapper():
        print("Before execution of decorator!")
        func()
        print("After execution of decorator!")
    return wrapper

@greet_decorator
def message():
    print("This is my first attempt at using decorator.")

message()