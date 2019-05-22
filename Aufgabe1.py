def r_fac(n):
	if n == 1:
		return 1
	return n*r_fac(n-1)

def i_fac(var):
	result = 1
	for i in range(1,var):
		result = result*i
	return result*var



var = int(input())
signal = True
while signal:
	if var < 0:
		print("Ihre Eingabe war keine natürliche Zahl! Versuchen Sie es nochmal!!!1")
		var = int(input())
	else:
		signal = False
		print("Die Fakultät von", var , "ist", r_fac(var) )
		print("iterativ gelöst : ", i_fac(var))




