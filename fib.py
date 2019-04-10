
import sys, math

S = int((sys.argv[1]))

fib = [0, 1]

for i in range(0,S-2,1):
	fib.append(fib[i] + fib[i+1])
print fib
