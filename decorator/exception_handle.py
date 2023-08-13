# Implements a decorator to handle exceptions raised by a function and provide a default response.

class negativeException(ValueError):
    pass

def custom_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            if func(*args, **kwargs) < 0:
                raise negativeException(f"{negativeException.__name__} This is a negative number")
        except Exception as error:
            return f"Error: {error}"
        return func(*args, **kwargs)
    return wrapper

@custom_exceptions
def subtraction(x,y):
    return y-x

#print (subtraction(5,0))


##### default response

def response_exception(response):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if result < 0:
                    raise ValueError ("This is a negative value!")
            except Exception as error:
                print (f"Error: {error}")
                return response
            return result
        return wrapper
    return decorator

@response_exception("ERROR FOUND!")        
def division(x:int, y:int) -> int:
    return x/y

print (division(-2,0))