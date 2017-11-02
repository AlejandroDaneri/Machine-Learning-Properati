# Mejor Resultado de predicción

Random Forest : 0.74796

# Ideas:

* Crear un nuevo dataframe con el id de cada publicacion, agregar columna de "a estrenar" y "patio" y verificar
usando la descripcion del anuncio si la propiedad posee estas caracteristicas o no, luego evaluar el impacto
que tienen en el costo de la propiedad, si sustancialmente aumenta su valor o no.

* Analizar el tamaño de la superficie en venta en cada zona, y si en las zonas con mayor valor se suelen vender terrenos mas
pequeños (Establecer un valor a "terreno pequeño").

# Informe TP1

https://www.overleaf.com/11119244fyxkxxddzmyk

# Informe TP2

https://www.overleaf.com/10733034vsbywgtyrfbw

# Ejemplo de comando para juntar CSVs

{ head -n1 properati-AR-2013-08-01-properties-sell.csv; for f in *.csv; do tail -n+2 "$f"; done; } > ../new.csv

## Paginas útiles

* https://data.buenosaires.gob.ar

* http://datosabiertos.aeroterra.com

* http://blog.properati.com.ar/buenos-aires-en-3d/

* http://datos.jus.gob.ar/dataset
