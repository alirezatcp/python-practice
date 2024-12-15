# string funcs
string = 'Hello, world.'
my_list = ['Hello', 'world']

length = len(string)
print(length) # 13

upper = string.upper()
print(upper) # HELLO, WORLD.

lower = string.lower()
print(lower) # hello, world.

count_l = string.count('l')
print(count_l) # 3

is_ends_with = string.endswith('.')
print(is_ends_with) # True

is_starts_with = string.startswith('H')
print(is_starts_with) # True

index_of_first_o = string.find('o')
print(index_of_first_o) # 4

index_of_last_o = string.rfind('o')
print(index_of_last_o) # 8

is_just_numbers_and_letters = string.isalnum()
print(is_just_numbers_and_letters) # False 

is_just_numbers = string.isnumeric()
print(is_just_numbers) # False

list_to_str = ','.join(my_list) # tuple can use too
print(list_to_str) # Hello,world

str_to_list = string.split(' ')
print(str_to_list) # ['Hello,', 'world.']

str_to_list_with_list_len = string.split(' ', maxsplit=0)
print(str_to_list_with_list_len) # ['Hello, world.']

# some example to see deference with ' ' and nothing
s = 'hello          world.  '
example1 = s.split()
print(example1) # ['hello', 'world.']

example2 = s.split(' ')
print(example2) # ['hello', '', '', '', '', '', '', '', '', '', 'world.', '', '']

replace_l_with_h = string.replace('l', 'h')
print(replace_l_with_h) # Hehho, worhd.

replace_one_l_with_h = string.replace('l', 'h', 1)
print(replace_one_l_with_h) # Hehlo, world.

strip = string.strip('.') # if string start or end with '.' clear that. (how many '.' clear all just in start and end.)
print(strip) # Hello, world

right_strip = string.rstrip('.')
print(right_strip) # Hello, world

left_strip = string.lstrip('H')
print(left_strip) # ello, world.

capitalize = 'hello, world'.capitalize()
print(capitalize) # Hello, world

title = string.title()
print(title) # Hello, World.

is_instance = isinstance(string,str)
print(is_instance) # True

instance_type = type(string)
print(instance_type) # <class 'str'>


# formatting strings (f string)
print('\nf strings:\n')

import datetime
my_name = 'Alireza'
today = datetime.datetime.today()
print(f'''
Hello,
\tmy name is {my_name}.
\ttoday we are in {today:%Y-%m-%d.}
        ''')


# asci code
print(ord('a')) # 97
print(chr(97)) # a

string = "print('This is a python code: ', 5**2)"
exec_code = eval(string) # convert text to python code