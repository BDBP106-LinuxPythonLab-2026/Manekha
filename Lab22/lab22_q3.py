def count_calls(func):
    count=[0]
    def wrapper():
        func()
        count[0]+=1
        print(f"Call count: {count[0]}")
    return wrapper

@count_calls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()
