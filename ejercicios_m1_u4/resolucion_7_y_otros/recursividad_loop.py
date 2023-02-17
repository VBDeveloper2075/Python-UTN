# ##############################################
# Recursión ####
# ##############################################
def mi_suma(L):
	return 0 if not L else L[0] + mi_suma(L[1:]) # Uso de expresión ternaria

print(mi_suma([1, 2, 3, 4, 5]))	
print('',end='\n################\n' )	
	
L = [1, 2, 3, 4, 5]
suma = 0
while L:
	suma += L[0]
	L=L[1:]
print(suma)

 