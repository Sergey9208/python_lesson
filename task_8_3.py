from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num_list = [element for element in(*args, *kwargs.values())]
        n = [f'{func.__name__}({element}: {type(element)}'for element in num_list]
        print(n, func(args, kwargs))
    return wrapper


@type_logger
def calc_cube(*x, **y):
    num_list = [element for element in (*x, *y.values()) if isinstance(element, int) or isinstance(element, float)]
    return [i ** 3 for i in num_list]

a = calc_cube(4, 11, 20, 8.6, 7)
