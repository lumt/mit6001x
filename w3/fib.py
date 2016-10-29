"""
Memoization example
Using Fibonacci
"""

# Here is a function to calculate fib(n) using recursion
def fib(n):
	global numfibcalls
	numfibcalls += 1
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

# Here is the same function using Memoization
def fib_mem(n, d):
	global numfibcalls1
	numfibcalls1 += 1
	if n in d:
		return d[n]
	else:
		ans = fib_mem(n-1, d) + fib_mem(n-2, d)
		d[n] = ans
		return d[n]

# Declare d with base case:
d = {1:1, 2:1}
# 1) does look up first to see if nth term exists in d
# 2) else computes it, adds to d and returns the ans

# much more efficient than recursion as function is presumably
# called less amounts of time.

numfibcalls = 0
fibarg = 31
print(fibarg, 'term in fib is: ', fib(fibarg))
print('recursion calls: ', numfibcalls)

numfibcalls1 = 0
print(fibarg, 'term in fib is: ',fib_mem(fibarg,d))
print('Memoization calls: ', numfibcalls1)