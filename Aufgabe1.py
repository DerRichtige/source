def r_fac(n):
	if n == 1:
		return 1
	if n == 0:
		return 1
	return n*r_fac(n-1)

def i_fac(var):
	if var == 0:
		return 1
	result = 1
	for i in range(1,var+1):
		result = result*i
	return result


var = int(input("Geben Sie eine Zahl ein : "))
signal = True
while signal:
	if var < 0:
		var = int(input("Ihre Eingabe war keine natürliche Zahl! Versuchen Sie es nochmal!!!1 : "))
	else:
		signal = False
		print("Die Fakultät von", var , "ist", r_fac(var) )
		print("iterativ gelöst : ", i_fac(var))




