from functools import reduce

func = lambda a: a*2 # a function with input a and return a*2
print(func(3)) # 6

list1 = [1, 2, 3, 4]
map_list = list(map(func, list1)) # send list variables to func one by one and make new list
print(map_list) # [2, 4, 6, 8]

func2 = lambda a: a%2 == 0 # a function with input a and return if a%2 True and if not return False
filter_list = list(filter(func2, list1)) # send list variables to fuck one by one and if result is True add to filter_list
print(filter_list) # [2, 4]

func3 = lambda a, b : a*b # a function to get a and b and return multiple of them
reduce_result = reduce(func3, list1) # send 2 list variables to func and replace result with 2 of them and do this till reach a number
print(reduce_result) # 24