#Iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

for num in range(0,50):
    if num % 3 == 0 and num % 5 == 0:
        print (f"{num}: FizzBuzz!")
    elif num % 3 == 0:
        print (f"{num}: Fizz")
    elif num % 5 == 0:
        print (f"{num}: Buzz")
    else:
        print (f"{num}")
    