import os 

print(os.getcwd()) # get this file directory path.

# create new file with name text_file
text_file = open(file='./text_file', mode='w')

# write text in text_file
write = text_file.write('''Hi...
this is a test file.
we create that with codes in ./text-files.py
#write

''')

print(write) # length of text we writed

# we can print text inside a file like this:
print('I add this line with #print\n', file=text_file)

# write a list in file
write_list = ['this', ' line', ' by', ' #writelines\n']
write_line = text_file.writelines(write_list)
print(write_line) # return None

# shows pointer index
print(text_file.tell())

# close file
text_file.close()

print('\nreading file:\n')

# read text_file
with open('text_file', 'r+') as text_file:
    
    print('pointer is in: ',text_file.tell())

    print(text_file.readline()) # read a line from file. from where pointer is to end of line

    print('pointer is in: ',text_file.tell())

    print(text_file.read()) # read all file. from where pointer is to end of file

    print('pointer is in: ',text_file.tell())

    print(text_file.readlines()) # read all file. from where pointer is to end of file and return that in a list.

    s = text_file.seek(0) # get pointer to first of text
    print(f'pointer comes to {s} with seek')

    print('pointer is in: ',text_file.tell())

    print(text_file.readlines())

    print('pointer is in: ',text_file.tell())