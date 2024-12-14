list1 = list('alireza')
print(list1) # ['a', 'l', 'i', 'r', 'e', 'z', 'a']

list2 = 'this,is,list,2'.split(',')
print(list2) # ['this', 'is', 'list', '2']

l1 = [1,2,3]
l2 = [3,4,5]
print(l1+l2) # [1, 2, 3, 3, 4, 5]
print(l1*2) # [1, 2, 3, 1, 2, 3]

print(l1<l2) # compare l1[0] with l2[0] and return True
print(l1>l2) # False

args = [1,2,3,4,5]
print(*args) # 1 2 3 4 5

list_for_sort = [4, 3, 2, 5, 6]
print(list_for_sort.sort()) # None
print(list_for_sort) # [2, 3, 4, 5, 6]

list_for_sort = [4, 3, 2, 5, 6]
new_list = sorted(list_for_sort) # options: reverce=True (sort reverse), key=len(sort with length. we can write our func too.)
print(list_for_sort, new_list) # [4, 3, 2, 5, 6] [2, 3, 4, 5, 6]

# perception

plist1 = [x**2 for x in range(1,11)] # square numbers 1 to 10
print(plist1) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

plist2 = [x**2 for x in range(1,11) if x%2 ==0] # square numbers 1 to 10 (just even numbers)
print(plist2) # [4, 16, 36, 64, 100]

plist3 = [(x, x**2) for x in range(1,11) if x%2 ==0] # a list from tuples of numbers and their square numbers 1 to 10 (just even numbers)
print(plist3) # [(2, 4), (4, 16), (6, 36), (8, 64), (10, 100)]

plist4 = [(x,y) for x in [1,2,3,4] for y in [1,3,2,6] if x != y] # a list from tuples of two list if 2 of them not equal
print(plist4) # [(1, 3), (1, 2), (1, 6), (2, 1), (2, 3), (2, 6), (3, 1), (3, 2), (3, 6), (4, 1), (4, 3), (4, 2), (4, 6)]

plist5 = [abs(x) for x in [-2, -4]] # male that list absolute 
print(plist5) # [2, 4]

plist6 = [10, 3, 5, 7, 8, 9]
plist6 = [x if x>5 else 0 for x in plist6] # write number if number>6 or 0 to else
print(plist6) # [10, 0, 0, 7, 8, 9]

from random import randrange
plist7 = [randrange(80, 120) for i in range(10)] # 10 random numbers from 80 to 120
print(plist7) # [117, 82, 114, 119, 102, 109, 110, 110, 106, 99]

plist8 = [num for i in range(10) if (num := randrange(80, 120)) > 100] # 10 random numbers from 80 to 120 if bigger than 100 (list length may be letter than 10)
print(plist8) # [118, 107, 105, 112, 113]

plist9 = [[1,2,3,4], [5,6,7,8]]
plist9 = [[row[i] for row in plist9] for i in range(4)] # change rows and columns
print(plist9) # [[1, 5], [2, 6], [3, 7], [4, 8]]

lista = ['a', 'b', 'c']
listb = [1, 2, 3, 4, 5]
zip_list = list(zip(lista, listb))
print(zip_list) # [('a', 1), ('b', 2), ('c', 3)]

plist10 = list(zip(*plist9)) # change rows and columns
print(plist10)

input_list = [x for x in input('Enter list parameters with space: ').split()] # input = 1 b 4
print(input_list) # ['1', 'b', '4']

input_list = [int (x) for x in input('Enter list numbers with space: ').split()] # input = 1 4 5
print(input_list) # [1, 4, 5]