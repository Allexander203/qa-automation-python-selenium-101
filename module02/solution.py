def num_add(a,b):

	return a+b

def num_sub(a,b):

	return a-b

def num_mul(a,b):

	return a*b

def num_div(a,b):

	return a/b

def num_floor(a,b):

	return a//b

def num_rem(a,b):

	return a%b

IS_TRUE = True 
IS_FALSE = False 

PANCAKE_INGREDIENTS = dict(
  flour = 2,
  eggs = 4,
  milk = 200,
  butter = False,
  salt = 0.001)

def ingredient_exists(ingr,dict):

	return ingr in dict

def fatten_pancakes(dict):
	dict_copy = dict.copy()
	dict_copy['butter'] = True
	dict_copy['eggs'] = 6
	return dict_copy

def add_sugar(dict):
	dict_copy = dict.copy()
	dict_copy['sugar']="sugar"
	return dict_copy

def remove_salt(dict):
	dict_copy = dict.copy()
	del dict_copy['salt']
	return dict_copy

FIBONACCI_NUMBERS = []
FIBONACCI_NUMBERS.append(1)
FIBONACCI_NUMBERS.append(1)
FIBONACCI_NUMBERS.append(2)
FIBONACCI_NUMBERS.append(3)
FIBONACCI_NUMBERS.append(5)
FIBONACCI_NUMBERS.append(8)
FIBONACCI_NUMBERS.append(13)
FIBONACCI_NUMBERS.append(21)
FIBONACCI_NUMBERS.append(34)
FIBONACCI_NUMBERS.append(55)
FIBONACCI_NUMBERS.append(89)
FIBONACCI_NUMBERS.append(144)

# print(FIBONACCI_NUMBERS)

def add_fibonacci(lst):
	# print(lst)
	lst.append(lst[-1]+lst[-2])
	return lst

def fib_exists(lst, n):
	print(bool(n in lst))
	print('тест n-> ',n)
	return bool(n in lst)

def which_fib(lst, n):
	print(lst, n)
	return lst.index(n-1)
