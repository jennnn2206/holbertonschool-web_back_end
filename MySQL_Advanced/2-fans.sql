-- sumar los fans de todas las bandas por país de origen (sin eliminar duplicados) y ordenar de mayor a menor.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin 
ORDER BY nb_fans DESC