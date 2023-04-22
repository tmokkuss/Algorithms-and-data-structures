import math

stack = []

for token in input().split():
    if token.isdigit():
        stack.append(int(token))
    elif token == '+':
        stack.append(stack.pop() + stack.pop())
    elif token == '-':
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)
    elif token == '*':
        stack.append(stack.pop() * stack.pop())
    elif token == '/':
        b, a = stack.pop(), stack.pop()
        stack.append(a // b)
    elif token == '!':
        stack.append(math.factorial(stack.pop()))
    elif token == '#':
        value = stack.pop()
        stack.append(value)
        stack.append(value)
    elif token == '@':
        c, b, a = stack.pop(), stack.pop(), stack.pop()
        stack.append(b)
        stack.append(a)
        stack.append(c)
    elif token == '_':
        stack.append(-stack.pop())

print(stack.pop())
