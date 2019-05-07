T = True
F = False

if F: # Syntax Errors
    while True: print('Hello world')

if F: # ZeroDivisionError: division by zero
    10 * (1/0)

if F: # NameError: name 'spam' is not defined
    4 + spam*3

if F: # TypeError:  Can't convert 'int' object to str implicitly
    '2' + 2

if F: # Handling Exceptions 
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

if F: # 
    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

if T: # 
    import sys

    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.") # 注释在 txt 里面是没有用的
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


if F: # read file and strip
    import sys

    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
        print(i)
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise



if F: # get arg from sys input
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()



if F: # except Exception as XX
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst: # must do this: except Exception as XX
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                             # but may be overridden in exception subclasses
        x, y = inst.args     # unpack args
        print('x =', x)
        print('y =', y)

if F: # except ZeroDivisionError as xx
    def this_fails():
        x = 1/0

    try:
        this_fails()
    except ZeroDivisionError as xx:
        print('Handling run-time error:', xx)

if F: # Raising Exceptions
    raise NameError('HiThere')

if T:
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise
