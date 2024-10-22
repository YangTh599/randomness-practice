# Thayer Yang
# 22 OCT 2024
# Randomness Practice

from time import sleep
import random as ran

# Uses randrange() method
def randomRangeElement(list):
    index = ran.randrange(0,len(list)-1)
    item = list[index]

    print(f'{item} is at index {index}!')

# Uses randint() method
def randomIntElement(list):
    index = ran.randint(0,len(list)-1)
    item = list[index]

    print(f'Index {index}: {item}')


# 1 Random Color selector

colors = ['green','red','blue','yellow','orange']

print(colors)
randomRangeElement(colors)


sleep(1)

print()

# 2 Random Animal Index

animals = ['giraffe', 'hippopotamus', 'penguin', 'lion', 'panther']

print(animals)
for i in range(3):
    randomRangeElement(animals)
    sleep(.75)

print()

# 3 Random number for a list
    
numbers = [1,2,3,4,5,6,7,8,9,0]

ran.shuffle(numbers)

print(numbers)
randomRangeElement(numbers)
sleep(1)

print()

# 4 Random Fruit Selector

fruits = ['apple', 'orange', 'pear', 'strawberry', 'banana', 'kiwi', 'melon', 'grapefuit']

print(fruits)
randomIntElement(fruits)
sleep(1)

print()

# 5 Random Score Generator

names = ['Thayer', 'Lucas', 'Apollos', 'Joshua', 'Isaac']

for name in names:
    score = ran.randint(0,100)
    print(f'{name} got a score of {score}!')
    sleep(.75)

print()

# 6 Random Movie Selector
    
movies = ['Shrek', 'Shrek 2', 'Shrek 3', 'Shrek Forever After', 'Finding Nemo']

print(movies)
randomIntElement(movies)