##crear matriz
m1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]

##Suma de cada columna
sumaColumna = [sum(m1[columna][filas] 
                   
    for columna in range(len(m1))) 

        for filas in range(len(m1[0]))]

##Suma mas altas de las columnas
sumaAltaColumna = max(sumaColumna)

#Suma de cada fila 
sumaFilas = [sum(filas) for filas in m1]

##La suma de las filas
sumaBajaFilas = min(sumaFilas)

print("La suma mas alta de las columnas es:", sumaAltaColumna)
print("La suma mas baja de las filas es:", sumaBajaFilas)

