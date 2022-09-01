#dque means double ended queue and to use dque in stack implementation we need to import deque file from collections

from collections import deque
stack = deque()
stack.append("abc")
stack.append("x")
stack.append("y")
stack.append("z")
print(stack)

print(stack.pop())
print(stack)

