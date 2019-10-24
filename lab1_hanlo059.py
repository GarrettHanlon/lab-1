
def left(e): 			# left side of equation
    return e[0]						
def op(e):				# operator 
    return e[1]
def right(e):			# right side of equation
    return e[2]

def solving(v,q):
	if v == left(q):
		return q
	if op(left(q)) == '+':
		return solvingAdd(v,q)
	if op(left(q)) == '-':
		return solvingSubtract(v,q)
	if op(left(q)) == '*':
		return solvingMultiply(v,q)
	if op(left(q)) == '/':
		return solvingDivide(v,q)

def solvingAdd(v,q): 	#solves for addition problems
	A = left(left(q))
	B = right(left(q))
	C = right(q)
	if isInside(v,A):
		equation = (A, '=', (C, '-', B))
		return solving(v,equation)
	elif isInside(v,B):
		equation = (B, '=', (C,'-',A))
		return solving(v,equation)
	else:
		return None

def solvingSubtract(v,q):		#solves for subraction problems
	A = left(left(q))
	B = right(left(q))
	C = right(q)
	if isInside(v,A):
		equation = (A, '=', (C, '+', B))
		return solving(v,equation)
	elif isInside(v,B):
		equation = (B, '=', (A,'-',C))
		return solving(v,equation)
	

def solvingMultiply(v,q):		#solves for multiplication problems
	A = left(left(q))
	B = right(left(q))
	C = right(q)
	if isInside(v,A):
		equation = (A, '=', (C, '/', B))
		return solving(v,equation)
	elif isInside(v,B):
		equation = (B, '=', (C,'/',A))
		return solving(v,equation)
	else:
		return None

def solvingDivide(v,q):	#solves for division problems
	A = left(left(q))
	B = right(left(q))
	C = right(q)
	if isInside(v,A):
		equation = (A, '=', (C, '*', B))
		return solving(v,equation)
	elif isInside(v,B):
		equation = (B, '=', (A,'/',C))
		return solving(v,equation)
	else:
		return None

def solve(v,q):	
	if isInside(v, left(q)):
		return solving(v,(q))
	if isInside(v, right(q)):
		return solving(v,(right(q), op(q), left(q)))
	else:
		return None

	
def isInside(v, e):	#checks to see if variable is in side of equation
	if len(e) == 1:
		if(v == e):
			return True
		return False
	if(isInside(v,left(e))):
		return True
	if(isInside(v,right(e))):
		return True
	else:
		return False



print(isInside('x', 'x'))                      #  True   1 point
print(isInside('x', 'y'))                          #  False  1 point
print(isInside('x', ('x', '+', 'y')))            #  True   2 points
print(isInside('x', ('a', '+', 'b')))            #  False  2 points
print(isInside('+', ('a', '+', 'b')))            #  False  2 points
print(isInside('x', (('m', '*', 'x'), '+', 'b')))  #  True   2 points   


print(solve('x', (('a', '+', 'x'), '=', 'c')))
#  ('x', '=', ('c', '-', 'a'))  2 points
print(solve('x', (('x', '+', 'b'), '=', 'c')))
#  ('x', '=', ('c', '-', 'b'))  2 points

print(solve('x', (('a', '-', 'x'), '=', 'c')))
#  ('x', '=', ('a', '-', 'c'))  2 points

print(solve('x', (('x', '-', 'b'), '=', 'c')))
#  ('x', '=', ('c', '+', 'b'))  2 points

print(solve('x', (('a', '*', 'x'), '=', 'c')))
#  ('x', '=', ('c', '/', 'a'))  2 points

print(solve('x', (('x', '*', 'b'), '=', 'c')))
#  ('x', '=', ('c', '/', 'b'))  2 points

print(solve('x', (('a', '/', 'x'), '=', 'c')))
#  ('x', '=', ('a', '/', 'c'))  2 points

print(solve('x', (('x', '/', 'b'), '=', 'c')))
#  ('x', '=', ('c', '*', 'b'))  2 points

print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('y', '=', (('m', '*', 'x'), '+', 'b'))  2 points

print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('x', '=', (('y', '-', 'b'), '/', 'm'))  2 points

print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))
# ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))  5 points
print(isInside('x', 'x'))                          #  True   1 point
print(isInside('x', 'y'))                          #  False  1 point
print(isInside('x', ('x', '+', 'y')))              #  True   2 points
print(isInside('x', ('a', '+', 'b')))              #  False  2 points
print(isInside('+', ('a', '+', 'b')))              #  False  2 points
print(isInside('x', (('m', '*', 'x'), '+', 'b')))  #  True   2 points

print(solve('x', (('a', '+', 'x'), '=', 'c')))
#  ('x', '=', ('c', '-', 'a'))  2 points

print(solve('x', (('x', '+', 'b'), '=', 'c')))
#  ('x', '=', ('c', '-', 'b'))  2 points

print(solve('x', (('a', '-', 'x'), '=', 'c')))
#  ('x', '=', ('a', '-', 'c'))  2 points

print(solve('x', (('x', '-', 'b'), '=', 'c')))
#  ('x', '=', ('c', '+', 'b'))  2 points

print(solve('x', (('a', '*', 'x'), '=', 'c')))
#  ('x', '=', ('c', '/', 'a'))  2 points

print(solve('x', (('x', '*', 'b'), '=', 'c')))
#  ('x', '=', ('c', '/', 'b'))  2 points

print(solve('x', (('a', '/', 'x'), '=', 'c')))
#  ('x', '=', ('a', '/', 'c'))  2 points

print(solve('x', (('x', '/', 'b'), '=', 'c')))
#  ('x', '=', ('c', '*', 'b'))  2 points

print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('y', '=', (('m', '*', 'x'), '+', 'b'))  2 points

print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('x', '=', (('y', '-', 'b'), '/', 'm'))  2 points

print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))
# ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))  5 points




