T = True
F = False

if F: # list
    l1 = [1,2,3,4,5,6,7,7,8]
    print("0. ",l1.index(8))
    print("0.5. ",l1.count(7))
    print("1. ",l1)
    l1.append(9)
    print("2. ",l1)
    l1.extend([10,11,12])
    print("3. ",l1)
    l1.insert(0,0)
    print("4. ",l1)
    l1.insert(2,1.5)
    print("5. ",l1)
    l1.remove(1.5)
    print("6. ",l1)
    print("7. ",l1.pop(0))
    print("8. ",l1)
    l1.reverse()
    print("8.5. ",l1)
    l2 = l1.copy()
    l1.clear()
    print("9. ",l1)
    print("9. ",l2)

    squares = []
    for i in range(10):
        squares.append(i**2)
    print("10. ",squares)

if F: # lambda
    def makeLambda(y): 
        return lambda x,z:x**(y*z)
    lambdaFunc = makeLambda(2)
    print(lambdaFunc(10,2))

if F: # [for]
    p = 5
    squares1 = [p**x for x in range(10)]
    print(squares1)

if F: # [for for]
    combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print(combs)

if F: # del
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    print(a)
    del a[2:4]
    print(a)
    del a[:] # eq to a.clear()
    print(a)
    del a # make a undefined
    print(a)

if F: # Tuples and Sequences
    t = 12345, 54321, 'hello!'
    print(t[0])
    print(t)
    u = t, (1, 2, 3, 4, 5)
    print(u)
    v = ([1, 2, 3], [3, 2, 1])
    print(v)
    empty = ()
    singleton = "hello",
    print(empty)
    print(singleton)
    print(len(empty))
    print(len(singleton))

if F: # Set
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)                      # show that duplicates have been removed
    print('orange' in basket)                 # fast membership testing
    print('crabgrass' in basket)                 # fast membership testing
    a = set('abracadabra')
    b = set('alacazam')
    print(a)                                  # unique letters in a
    print(a - b)                              # letters in a but not in b
    print(a | b)
    print(a & b)
    print(a ^ b)  
    # Similarly to list comprehensions, set comprehensions are also supported:
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)

if F: # Dictionaries
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print("1. ",tel)
    print("2. ",tel['jack'])
    del tel['sape']
    tel['irv'] = 4127
    print("3. ",tel)
    print("4. ",list(tel))
    print("5. ",sorted(tel))
    print("6. ",'guido' in tel)
    print("7. ",'jack' not in tel)
    #The dict() constructor builds dictionaries directly from sequences of key-value pairs:
    print("8. ",dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
    # In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
    print("9. ",{x: x**2 for x in (2, 4, 6)})
    #When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
    print("10. ",dict(sape=4139, guido=4127, jack=4098))

if T: # Looping Techniques
    print("1. ")
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v, end=", ")

    print("\n2. ")
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v, end=", ")

    print("\n3. ")
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

    print("\n4. ")
    for i in reversed(range(1, 10, 2)):
        print(i, end=" ")

    print("\n5. ")
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f, end=" ")

    print("\n6. ")
    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
    print(filtered_data, end=" ")