import random
def check_number_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) is int:
            modified_result = result + 10
        else:
            modified_result = result
        return modified_result
    return wrapper

@check_number_decorator
def get_number(number):
    return number
number = 32
print(get_number(number))
