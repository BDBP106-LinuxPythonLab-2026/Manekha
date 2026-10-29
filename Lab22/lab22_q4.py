def check_positive(func):
    def wrapper(number):
        if number > 0:
            func(number)
        else:
            print("Number must be positive")
    return wrapper


@check_positive
def display_number(number):
    print("The number is:", number)


display_number(5)
display_number(-3)
display_number(0)