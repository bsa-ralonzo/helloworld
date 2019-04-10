
import sys, math

fib = [0, 1]

def fun(N):
	for i in range(0,S-2,1):
		fib.append(fib[i] + fib[i+1])

S = int((sys.argv[1]))
fun(S)
print fib




