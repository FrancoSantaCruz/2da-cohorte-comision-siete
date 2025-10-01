Algoritmo CondicionalesColores
	Definir color_uno, color_dos, color_tres Como Caracter
	
	color_uno = "Negro"
	color_dos = "Blanco"
	color_tres = "Azul"
	
	Si color_uno == color_dos Entonces
		Imprimir "Los colores 1 y 2 son IGUALES"
	SiNo 
		Si color_uno == color_tres Entonces
			Imprimir "Los colores 1 y 3 son IGUALES"
		SiNo 
			Si color_dos <> color_tres Entonces
				Imprimir "Los colores 2 y 3 son IGUALES"
			SiNo
				Imprimir "Los colores son todos distintos"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
