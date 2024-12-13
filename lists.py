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
