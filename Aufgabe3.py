import time 
var = input("geben Sie ihr Geburtstag ein mit Leerzeichen getrennt : ")
l1 = var.split()
t = time.localtime()
a = time.asctime(t)
l2 = a.split()
y = int(l2[4]) - int(l1[2])
m = 5 - l1[1]
d = int(l2[2]) - int(l1[0])
print ("Sie sind ca.", d+m*30+y*365, "Jahre alt ...")
