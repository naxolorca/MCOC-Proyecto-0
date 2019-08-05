# MCOC-Proyecto-0
MCOC-Proyecto-0

Introducción
==============

En el proyecto 0 se busca mostrar con un ejemplo la perdida de significancia al utilizar los numeros float16, float32, y float64.


Calculo de volumen y recuperacion del radio
==============

Podemos ver en este ejemplo que se calcula el volumen aproximado en kilometros de los planetas del sistema solar utilizando un radio "real", los volumenes se almacenan en float16, float32 y float64. Luego se procede a calcular los radios utilizando los volumenes guardados y se calculo su error.

Resultados
==============

Se define el error relativo como 

	ERROR = (Promedio_Calculado - Resultado_Exacto) / Resultado_Exacto

Podemos ver en el output que mientras menor es la capacidad de almacenar decimales, el error aumenta de forma significativa. Esto se nota en la diferencia del  radio en float32 y float16 nisiquiera es capas de almacenar el numero.
![Results](loss-of-significance.png)

Output de la consola:

	Usando float16

	Mercurio valor real = 2439.7 valor calculado = inf (error = inf )
	Jupiter valor real = 69911.0 valor calculado = inf (error = inf )
	Tierra valor real = 6371.0 valor calculado = inf (error = inf )
	Neptuno valor real = 24622.0 valor calculado = inf (error = inf )
	Venus valor real = 6051.8 valor calculado = inf (error = inf )
	Marte valor real = 3389.5 valor calculado = inf (error = inf )
	Urano valor real = 25362.0 valor calculado = inf (error = inf )
	Saturno valor real = 58232.0 valor calculado = inf (error = inf )

	Usando float32

	Mercurio valor real = 2439.7 valor calculado = 2439.70001318 (error = 5.4006384026e-09 )
	Jupiter valor real = 69911.0 valor calculado = 69910.998934 (error = 1.52485044679e-08 )
	Tierra valor real = 6371.0 valor calculado = 6371.00001861 (error = 2.92041603847e-09 )
	Neptuno valor real = 24622.0 valor calculado = 24622.0002742 (error = 1.11353615537e-08 )
	Venus valor real = 6051.8 valor calculado = 6051.80001063 (error = 1.75608656904e-09 )
	Marte valor real = 3389.5 valor calculado = 3389.50003054 (error = 9.01052084765e-09 )
	Urano valor real = 25362.0 valor calculado = 25362.0000058 (error = 2.29927949105e-10 )
	Saturno valor real = 58232.0 valor calculado = 58231.9996946 (error = 5.24446244329e-09 )

	Usando float64

	Mercurio valor real = 2439.7 valor calculado = 2439.7 (error = 3.72789565017e-16 )
	Jupiter valor real = 69911.0 valor calculado = 69911.0 (error = 6.24447450117e-16 )
	Tierra valor real = 6371.0 valor calculado = 6371.0 (error = 5.71021630371e-16 )
	Neptuno valor real = 24622.0 valor calculado = 24622.0 (error = 5.91012721484e-16 )
	Venus valor real = 6051.8 valor calculado = 6051.8 (error = 4.50854969648e-16 )
	Marte valor real = 3389.5 valor calculado = 3389.5 (error = 4.02490648373e-16 )
	Urano valor real = 25362.0 valor calculado = 25362.0 (error = 5.73768442093e-16 )
	Saturno valor real = 58232.0 valor calculado = 58232.0 (error = 6.2473877028e-16 )

