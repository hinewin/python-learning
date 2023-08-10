#Implement a custom exception class called NegativeValueError that inherits from the built-in ValueError exception, and a function validate_positive. This custom exception should be raised when a function called validate_positive receives a negative value as its input with the error message "Input value is negative". Otherwise, return the same positive value.

class NegativeValueError(ValueError):
    pass

def validate_positive(value):
    if value <0:
        raise NegativeValueError("Input value is negative")
    else:
        return value
    
validate_positive(-3)


#When we define a custom exception, we often want it to inherit some properties from built-in exceptions. 
# This is done by specifying the built-in exception as a parameter (in parenthesis) on the custom exception definition line, using object-oriented programming concepts, specifically inheritance.

#Defining NegativeValueError(ValueError) means that NegativeValueError will be a subclass of the built-in Python exception ValueError.
#  This inherits properties from ValueError and can also be caught using except ValueError in a try/except block.

#ValueError is a built-in Python exception raised when a function receives an argument of the correct type but with an inappropriate value.
#  By inheriting from ValueError, our custom exception NegativeValueError signals that it's intended to be used in similar situations, but provides a more specific type that can be caught and handled separately if desired.

#So, ValueError is passed as the parameter to our custom exception NegativeValueError to allow for this inheritance and to provide additional details on the context and cause of the exception which helps in debugging.





