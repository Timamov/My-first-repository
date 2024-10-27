import random
def check_number_decorator(func):
    def wrapper(number):
        result = 0
        if type(number) is int:
            result = number + 10
        else:
            result = number
        return func(result)
    return wrapper

@check_number_decorator
def get_number(num):
    return num
number = 35
print(get_number(number))