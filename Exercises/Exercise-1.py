#Funcion que te dira el maximo de dos numeros
def max(A,B):
	if A>B:
		return A
	else:
		return B
	
A = int(input("Ingrese el primer numero: "))
B = int(input("Ingrese el segundo numero: " ))

print (max(A,B))

