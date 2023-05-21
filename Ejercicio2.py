import numpy as np

#Usamos array y especificamos [] ,
m = np.array([[1, 2], [3, 4]])

m_inversa = np.linalg.inv(m)

#Se imprime la matriz inversa
print("La matriz inversa es:")
print(m_inversa)

#Calcular la multiplicacion de ambas matrices
m_multiplicada = np.dot(m, m_inversa)

#Imprime resultado
print("multiplicacion de la matriz y su inversa:")
print(m_multiplicada)
