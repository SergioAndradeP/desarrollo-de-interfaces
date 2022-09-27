def funcion_fibonacci(n):
	if n<=1:
		return n
	else:
		return funcion_fibonacci(n-1) + funcion_fibonacci(n-2)
