def r_fib(n):
	if n == 1:
		return 1
	if n == 0:
		return 0
	return r_fib(n-1)+r_fib(n-2)

def i_fib(n):
	a, b, count = 0, 1, 0
	while count < n:
		a, b = b, a+b
		count += 1
	return a

var = int(input("Geben Sie eine Fibonacci Zahl ein : "))

while True:
	if var < 0:
		var = int(input("Geben Sie eine Fibonacci Zahl ein : "))
		continue
	else:
		print("Die ", var, "te Fibonacci Zahl ist : ", r_fib(var), "(Rekursiv)")
		print("Die ", var, "te Fibonacci Zahl ist : ", i_fib(var), "(Iterativ)")
		break

	
