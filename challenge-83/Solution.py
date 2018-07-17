
from timeit import Timer
t = Timer("for i in range(100):1+1")
print t.timeit()
