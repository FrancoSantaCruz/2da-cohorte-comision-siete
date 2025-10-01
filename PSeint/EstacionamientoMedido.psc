Algoritmo EstacionamientoMedido
	// Un usuario ingresa el valor que va a pagar para poder estacionar
	// su auto. El estacionamiento va a estar medido en 1000 pei.
	Definir precio_estacionamiento, monto_ingresado, vuelto Como Entero;
	
	precio_estacionamiento = 1000
	
	// Pedir al usuario cuanto va a pagar
	Imprimir "Debe abonar un total de ARS$1000 para estacionar libre de multas."
	Imprimir "Ingresa el valor a depositar: "
	Leer monto_ingresado
	
	Si monto_ingresado == precio_estacionamiento Entonces
		Imprimir "Puede pasar usted buen señor/a :D"
	SiNo
		Si monto_ingresado > precio_estacionamiento Entonces
			vuelto = monto_ingresado - precio_estacionamiento
			Imprimir "Gracias amigo, se ve que cobraste en estos días. Tu vuelto es de ARS$",vuelto,". Pase usted."
		SiNo
			Imprimir "Disculpe, usted sabe leer el mensaje anterior? Claramente dice ARS$1000. No sea ratón. Vuelva a su casa t(-.-t)"
		FinSi
	FinSi
	
FinAlgoritmo
