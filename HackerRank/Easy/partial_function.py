#Implement a function called partial that takes a function as its first argument, func, followed by an arbitrary number of positional and keyword arguments. The function should return a new function representing the partial application of the provided arguments to the function func. More formally, the function returned should take the remaining arguments if any, and return the value the function func would return if provided with the previous and current arguments.

#!/bin/python3

def partial(func: callable, *args, **kwargs) -> callable:
    def inner(*extra_args, **extra_kwargs):
        all_args = args + extra_args
        all_kwargs = kwargs.copy()
        all_kwargs.update(extra_kwargs)
        return func(*all_args, **all_kwargs)
    return inner()