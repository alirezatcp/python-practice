import time
from itertools import count

start_time = time.perf_counter() # gives current time

my_list = [1, 2, 3, 4]
print(dir(my_list)) # shows methods that my_list have.

my_iter = iter(my_list)
print(dir(my_iter)) # shows methods that my_iter have. (__next__ added.)
print(my_iter) # <list_iterator object at 0x7fd301a5d180>
print(next(my_iter), next(my_iter), next(my_iter), next(my_iter)) # get our list contents. if we use next one more time we face this error: StopIteration

counter = count(10) # we create a inf iter starts from 10
print(next(counter), next(counter)) # 10 11

end_time = time.perf_counter() # gives current time

print('Our program ended in ', end_time - start_time, ' seconds.') # gives time from start_time to end_time