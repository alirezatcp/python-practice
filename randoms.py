import random

print(random.random()) # every time we run this file create a new random float number (0 <= number < 1)

#####
random.seed(1) # after this just one time create a random number for all prints and show them every time we run this file
print(random.random())
print(random.random())
print(random.random())
#####

print(random.uniform(10, 15)) # a random float number between [10, 15)

print(random.randint(20, 25)) # a random int number between [20,25]

print(random.randrange(1, 11, 2)) # print random number starts from 1 with step 2 to 11

print(random.choice([2, 22, 222, 2222])) # choose a random number from given list

print(random.sample([1, 11, 111, 1111], 2)) # choose 2 value frome given list

my_list = [1, 2, 3, 4, 5]
print(random.shuffle(my_list)) # change indexes of my_list randomly (just change and print result is None)
print(my_list) # we should see new list