Algoritmo MientrasEstacionamientoMedido
	Definir precio_estacionamiento, monto_ingresado, vuelto Como Entero;
	
	precio_estacionamiento = 1000

	Imprimir "Debe abonar un total de ARS$1000 para estacionar libre de multas."
	Imprimir "Ingresa el valor a depositar: "
	Leer monto_ingresado
	
	Mientras monto_ingresado < precio_estacionamiento Hacer
		Imprimir "Disculpe, usted sabe leer el mensaje anterior? Claramente dice ARS$1000. No sea rat�n. Vuelva a su casa t(-.-t)"
		Imprimir "Ingresa el valor a depositar: "
		Leer monto_ingresado
	FinMientras
	
	Si monto_ingresado == precio_estacionamiento Entonces
		Imprimir "Puede pasar usted buen se�or/a :D"
	SiNo
		Si monto_ingresado > precio_estacionamiento Entonces
			vuelto = monto_ingresado - precio_estacionamiento
			Imprimir "Gracias amigo, se ve que cobraste en estos d�as. Tu vuelto es de ARS$",vuelto,". Pase usted."
		FinSi
	FinSi
	
FinAlgoritmo
