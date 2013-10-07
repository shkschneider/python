#!/usr/bin/env python

# staticmethod
class ClassExample:

    @staticmethod
    def staticExample():
        print 'ClassExample.staticExample()'

def staticmethod_example():
    ClassExample.staticExample()

# auth
def auth(func):
    def wrapper(*args, **kwargs):
        authenticated = True
        if not authenticated:
            raise Exception('403 Forbidden')
        return func(*args, **kwargs)
    return wrapper

@auth
def auth_example():
    print 'auth_example()'

# once
def once(name):
    callstack = []
    def wrapper(func):
        def wrapped(): #arg
            if name not in callstack:
                callstack.append(name)
                return func() #arg
            return None
        return wrapped
    return wrapper

@once('main')
def once_example():
    print 'once_example()'

if __name__ == '__main__':
    auth_example()
    once_example()
    once_example()
    staticmethod_example()

# EOF
