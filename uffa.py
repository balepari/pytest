import sys
import os

with open('settings.py', 'r') as f:
    a = f.read().splitlines()
f.close()
# f = open('settings.py', 'r')
# a = f.readlines()
print(a)
print(str(type(a)))
b = str(a)
print(b)
print(str(type(b)))
c = b.split(' = ')
print(c)
print(str(type(c)))


