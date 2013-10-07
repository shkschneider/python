#!/usr/bin/env python

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
def main():
    print 'Executed'

if __name__ == '__main__':
    print 'main()'
    main()
    print 'main()'
    main()
    print 'main()'
    main()

# EOF
