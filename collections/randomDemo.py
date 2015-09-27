__author__ = 'luowen'

""" random demos """

import random

print(random.random())
print(random.randrange(20, 333, step=1))  # random the start and end data the argument step is the step
print(random.randint(1, 455))
print(random.choice(range(1, 100)))

list1 = [i for i in range(1, 10)]
(random.shuffle(list1))
print(list1)  # shuffle the list1 collection

num1 = 2
num2 = 3
print(random.uniform(num1, num2))  # random a float type num which num1 < N < num2

stringList = ['ab', 'cd', 'ef', 'xyz']

string = random.choice(stringList)
print(string)  # random choice the item of stringList collection
