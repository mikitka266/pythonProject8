from typing import Callable

def deco(func: Callable):
    data = {}
    with open (f'{func.__name__}.json', 'r') as f:
        data = json.load(data, encoding='utf-8', errors='ignore', indent=2)


    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        for i in range(len(args)):
            data.update({i: args[i]})
        data.update({**kwargs})
        with open(f'{func.__name__}.json', 'a') as f:
            json.dump(data, f, indent=2)

    
    return wrapper


@deco
def roots(a: int, b: int, *args, **kwargs):
    return  a*b 

