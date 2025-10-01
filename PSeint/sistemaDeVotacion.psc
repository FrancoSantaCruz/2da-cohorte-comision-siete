Algoritmo sistemaDeVotacion
	// Una persona no puede votar antes de los 16 años. 
	// Una persona es OPCIONAL que vote entre los 16 y los 18 años
	// Una persona es OBLIGATORIO que vote entre los 18 y los 70 años
	// Una persona es OPCIONAL que vote de 70 hacia arriba.
	Definir edad Como Entero
	
	Imprimir "Ingresa tu edad para validar tu situación de voto: "
	Leer edad
	
	// 1-15 al 100
	Si edad < 16 Entonces
		Imprimir "No podes votar. Sos menor de edad."
	SiNo
		// 16-17 al 100
		Si edad >= 16 Y edad < 18 Entonces
			Imprimir "Es opcional tu voto, pero se agradece tu patriotismo."
		SiNo
			//18 al 69
			Si edad < 70 Entonces
				Imprimir "Es OBLIGATORIO tu voto, te espero en la mesa"
			SiNo
				// 70 al infinito
				Imprimir "Es opcional tu voto, se agradece el esfuerzo."
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
