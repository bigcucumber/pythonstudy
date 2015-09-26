__author__ = 'luowen'

""" deque collection type is convenient for implement deque operations and stack operations"""

from collections import deque

deque1 = deque()

deque1.append("a")
deque1.append("a1")
deque1.append("a2")
deque1.append("a3")
deque1.append("a4")
deque1.append("a5")

print('deque demo')
print(deque1)
deque1.popleft()
print(deque1)
deque1.popleft()
print(deque1)

stack = deque()
stack.append("b1")
stack.append("b2")
stack.append("b3")
stack.append("b4")
stack.append("b5")

print("stack demo")
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

print("--------------")
print(stack)
stack.rotate()
print(stack)

