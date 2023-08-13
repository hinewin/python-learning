# Create a decorator to convert the return value of a function to a specified data type.

def str_conv(func):
    def wrapper(*args, **kwargs):
        if args:
            print (f"Turning {args} into a string...")
        elif kwargs:
            print (f"Turning {kwargs} into a string...")
        result = func(*args, **kwargs)
        return str(result)
    return (wrapper)

@str_conv
def add(x,y):
    return x + y

#### Determine the data type to turn into

def data_conv(data_type):
    def dectorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return data_type(result)
        return wrapper
    return dectorator
    
@data_conv(int)
def subtract(x,y):
    return x - y 

print (subtract (10,5))
print (type(subtract(10,5)))



