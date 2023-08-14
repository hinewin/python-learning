# Implement a class called FibonacciIterator whose constructor takes a single argument, n, which represents the number of Fibonacci numbers to generate. The class object should be iterable and should return n Fibonacci numbers.

class fibonacciIterator():
    def __init__(self, num):
        self.num = num
        self.current = 0
        self.count = 0
        self.next = 1
    
    def __iter__(self): #allow an object to be used as an iterable item
        return self
    
    def __next__(self):
        if self.count > self.num:
            raise StopIteration
        else:
            result = self.current
            self.current, self.next = self.next, self.current + self.next
            self.count +=1 
            return result
        

fin = fibonacciIterator(2)
for num in fin:
    print (num)