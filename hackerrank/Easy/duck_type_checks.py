#Implement a function called process_data that takes a single argument, obj. The function should call the obj.process() method if the object has a process() method and return its result. If the object does not have a process() method, the function should return None.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'process_data' function below.
#
# The function is expected to return obj.process() or None.
# The function accepts an class object obj as parameter.
#

def process_data(obj):
    if hasattr(obj,"process") and callable(getattr(obj,"process")):
        return obj.process()
    else:
        return None

###Solution
#This function uses built-in Python functions hasattr() and getattr(). 
# hasattr(obj, 'process') checks whether the object obj has an attribute named 'process'. If it does, callable(getattr(obj, 'process')) is used to check if that attribute is callable.

#  If both conditions are true, obj.process() is called and its result is returned. If one of these conditions is not true, the function returns None.


# __call__() is a method that allow an object to be called 




