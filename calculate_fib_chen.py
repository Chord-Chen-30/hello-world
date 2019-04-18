def fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

N = input("nth fibonacci number: ")

print "answer:", fib(N)

# This is another try,
# because
# I am handsome, hahahahaha

# (I think I can write diary here, it's fun :)