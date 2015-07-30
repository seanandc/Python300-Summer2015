class A(object):
    def __init__(self):
        print "A"
        # swallow
        super(A, self).__init__()

class B(object):
    def __init__(self):
        print "B"
        # swallow
        super(B, self).__init__()

class C(A):
    def __init__(self,arg):
        print "C","arg=",arg
        arg = 'C' + arg
        super(C, self).__init__()

class D(B):
    def __init__(self,arg):
        print "D", "arg=",arg
        arg = 'D' + arg
        super(D, self).__init__()

class E(C,D):
    def __init__(self, arg):
        print "E", "arg=",arg
        arg = 'E' + arg
        super(E, self).__init__(arg)

if __name__ == '__main__':

    print "[ MRO ]: {}".format([i.__name__ for i in E.mro()])
    E('blah')
    
'''
NOTE:
1. what's going on here
2. what's the shared ancestor here?
3. how do we solve this?
4. what we really want
'''