import logging

from lista7.zad6.log import log

@log()
def add(a, b):
    return a + b
@log()
class User:
    def __init__(self, name):
        self.name = name


a = add(1,2)
u = User("Jan")

