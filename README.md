# Ejemplo de comando para juntar CSVs

{ head -n1 properati-AR-2013-08-01-properties-sell.csv; for f in *.csv; do tail -n+2 "$f"; done; } > ../new.csv

# Datasets descargados que pueden llegar a servir

https://mega.nz/#F!lFB0xBra!4NUx_QqgNUW0uGEgwuOUNg

# Datos

Ideas:

* Filtrar datos por tipo de propiedad , porcentaje de tipo de propiedad por zona/lugar. Hacer análisis
de cuanto la relación entre el tipo de propiedad de cada zona y el valor promedio del m2 de la zona.

* Crear un nuevo dataframe con el id de cada publicacion, agregar columna de "a estrenar" y "patio" y verificar
usando la descripcion del anuncio si la propiedad posee estas caracteristicas o no, luego evaluar el impacto
que tienen en el costo de la propiedad, si sustancialmente aumenta su valor o no.

* Hacer análisis de la variación de valor promedio por usd por m2 de las propiedades (por zona) a traves de los años.
Armar una tabla comparativa que compare cual tuvo un mayor indice de crecimiento en valor a traves de los años/meses.
(Tener en cuenta de descartar aquellas zonas de las cuales en un principio no se tienen datos).

* Analizar el tamaño de la superficie en venta en cada zona, y si en las zonas con mayor valor se suelen vender terrenos mas
pequeños (Establecer un valor a "terreno pequeño").

# Informe

https://www.overleaf.com/11119244fyxkxxddzmyk

## Paginas útiles


* https://data.buenosaires.gob.ar

* http://datosabiertos.aeroterra.com

* http://blog.properati.com.ar/buenos-aires-en-3d/

* http://datos.jus.gob.ar/dataset
