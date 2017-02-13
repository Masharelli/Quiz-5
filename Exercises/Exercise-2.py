
def max_of_Three(A,B,C):
	if  A > B or A > C :
		return A

	elif B > A or B > C:
		return B
		
	else :  
		return C

A = int(input("Ingrese el primer numero"))
B = int(input("Ingrese el segundo numero"))
C = int(input("Ingrese el tercer numero"))

print (max_of_Three(A,B,C))
