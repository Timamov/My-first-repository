import random
def check_number_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(*args) is int:
            modified_result = {'number': result + 10}
        else:
            modified_result = {'number': result}
        return modified_result
    return wrapper

@check_number_decorator
def get_number(num):
    return num
number = 35
print(get_number(number))
