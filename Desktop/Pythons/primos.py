n = int(input("Ingresa un número entero para conocer qué primo se encuentra en dicha posición: "))
if n == 1:
	print("El primer número primo es el 2.")
elif n > 1:
	primos = [2] 
	m = 1 #esta variable es la que hace correr el ciclo 'while'
	x = 2 
	while m < n: 
	    x += 1 #checamos la condición de ser primo de uno en uno a partir del 3 (ya que el 2 ya está listo)
	    esPrimo = True
	    for p in primos: #para cada uno de los elementos de la lista...
	        if x % p == 0:
	            esPrimo = False
	            continue 
	            """cuando el número sea dividido por primera vez por algún elemento 
	               de la lista, entonces se descarta que éste sea un primo"""
	    if esPrimo:
	        primos.append(x) #si ningún elemento de la lista divide al número, entonces lo agregamos a ésta
	        m += 1 #para que el ciclo se repita la cantidad que ingresamos de veces 

	print("El primo que se encuentra en la posición número " + str(n) + " es el " + str(primos[len(primos)-1]) + ".")
else:
	print("Eso no tiene ningún sentido.")