T = True
F = False

if F: # Scopes and Namespaces Example
    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            global spam   # don't do this, so silly!
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)


if F:
    class Complex:
        def __init__(self, realpart, imagpart):  # constructor func
            self.r = realpart
            self.i = imagpart
    
    complex = Complex("A","B")
    print(complex.r, complex.i)


if F: # class-obj-arg . . . 
    class X:
        def __init__(self, counters):
            self.counter = counters
    x = X(1)
    while x.counter < 10:
        x.counter = x.counter * 2
    print(x.counter)
    del x.counter

if T: # class Dog
    class Dog:
        kind = 'canine'         # class variable shared by all instances
        tricks = []
        def __init__(self, name):
            self.name = name    # instance variable unique to each instance

        def getType(self):
            return self.kind
        
        def getName(self):
            return self.name

        def addTrick(self,trick):
            self.tricks.append(trick)

        def getTricks(self):
            return self.tricks

    dog = Dog("Make")
    print(dog.getType())
    print(dog.getName())
    dog.addTrick("Run")
    dog.addTrick("Holk")
    print(dog.getTricks())


if T:
    pass
