def guess_the_name(name:str, n:int):
    """
    This is a function to guess name in n tries.

        n: number of tries we have.
    """
    counter = 1

    while counter < n:
        print()

        guess = input(f'Enter your {counter}st guess: ')


        if guess == name:
            yield 'Congratulations, guess is right!!!'
            break

        else:
            yield 'Ops, please try more...'
            counter += 1

    else:

        print()
        guess = input('Enter your last guess: ')

        if guess == name:
            yield 'Congratulations, guess is right!!!'

        else:
            yield 'Oh, you cant guess the name :('

# game = guess_the_name('alireza', 5)
# print(game)

# for step in game:
#     print(step)
    

def create_name_list(n):
    '''
    This is a function to create a list with names and in size n.

        n: len of our list.
    '''

    our_list = []

    while len(our_list) < n:
        name = yield
        our_list += [name]
        print(our_list)

cnl = create_name_list(5)

try:
    next(cnl)
    cnl.send('one')
    cnl.send('two')
    cnl.send('three')
    cnl.send('four')
    cnl.send('five')

except: 
    pass