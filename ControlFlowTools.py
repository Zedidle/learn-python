T = True
F = False

if F: # fibnacci
	def fib(n,a,b):
		if a < n:
			print(a,end=' ')
			fib(n,b,a+b)
	fib(10000000, 0 , 1)
	print("\n\n---------------------------------------------------------\n")

if F: # list
	fruits = ['Banana', 'Apple', 'Lime']
	loud_fruits = [fruit.lower() for fruit in fruits]
	print(loud_fruits)
	print(list(enumerate(fruits)))
	print("\n\n---------------------------------------------------------\n")

if F: # input
	name = input('What is your name?\n')
	print('Hi, %s.' % name)
	print("\n\n---------------------------------------------------------\n")

if F: # for
	numbers = [2,3,5,7]
	result = 1
	for n in numbers:
		result *= n
	print("result:",result)

if F: # def -> str & return
	def f(ham: str, eggs: str = 'eggs') -> str:
		print("Annotations:", f.__annotations__)
		print("Arguments:", ham, eggs)
		return ham + ' and ' + eggs
	print(f('spam'))

if F: # if-elif-else
	x = int(input("Please enter an integer:"))
	if x < 0:
		x = 0
		print("Negative changed to zero")
	elif x == 0:
		print("zero")
	elif x == 1:
		print("single")
	else:
		print("More")

if F: # for-in-range()-len()
	a = ["A","B","C","D","E","F","G"]
	for i in range(len(a)):
		print(i,a[i])


if F: # for-else  遍历到最后一项仍然未break,则触发else
	for n in range(2, 10):
		for x in range(2, n):
			if n % x == 0:
				print(n, 'equals', x, '*', n//x)
				break
		else:
			# loop fell through without finding a factor
			print(n, 'is a prime number')

if F: # More on defining Functions
	def ask_ok(prompt, retries=4, reminder='Please try again!'):
		yTuple = ('y', 'ye', 'yes')
		while True:
			ok = input(prompt)
			if ok in yTuple:
				return True
			if ok in ('n', 'no', 'nop', 'nope'):
				return False
			retries -= 1
			if retries < 0:
				raise ValueError('invalid user response')
			print(reminder)
	ask_ok("Please input your password:")


if F: # is None
	def f1(a, L=None):
		if L is None:
			L = []
		L.append(a)
		return L
	print(f1("A"))

if F: 
	pass

if F: # lambda expression
	def make_incrementor(n):
	    return lambda x: x + n
	print(make_incrementor(10)(10))


if T: # Keyword arguments
	def cheeseshop(kind, *arguments, **keywords):
		print("-- Do you have any", kind, "?")
		print("-- I'm sorry, we're all out of", kind)
		for arg in arguments:
			print(arg)
		print("-" * 40)
		for kw in keywords:
			print(kw, ":", keywords[kw])
	cheeseshop("Limburger", 
		"It's very runny, sir.",
		"It's really very, VERY runny, sir.",
		shopkeeper="Michael Palin",
		client="John Cleese",
		sketch="Cheese Shop Sketch")