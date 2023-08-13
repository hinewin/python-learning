#2. Create a decorator function to measure the execution time of a function.
import time
def executionTime(func):
    def wrapper(*args, **kwargs):
        print (f"Begin function...")
        start_time = (time.time())
        result = func(*args, **kwargs)
        eclapse_time = (time.time())
        print (f"End time: {round(eclapse_time - start_time,6)}")
        return result
    return wrapper

@executionTime
def test_function():
    i = 1
    while i < 5:
        if i > 5:
            break
        print (i)
        i+=1


test_function()