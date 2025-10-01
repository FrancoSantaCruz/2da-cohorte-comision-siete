Algoritmo MientrasPasswordIncorrecto
	//Mientras {condicion} Hacer
	//FinMientras
	//Definir valor Como Entero
	
	//valor = 1
	
	//Mientras valor<10 Hacer
	//	Imprimir valor
	//	valor = valor + 1
	//FinMientras
	
	Definir password_guardada, password_ingresada Como Caracter;
	password_guardada = "informatorio"
	
	Imprimir "Ingrese su contraseña: "
	Leer password_ingresada
	
	// <> -> Me va a dar verdadero siempre que sean DIFERENTES.
	Mientras password_guardada <> password_ingresada Hacer
		Imprimir "INCORRECTO! Ingrese su contraseña nuevamente: "
		Leer password_ingresada
	FinMientras
	
	Imprimir "Ingreso satisfactoriamente. Vaya a su perfil"
FinAlgoritmo
