# 10.	Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
# 	Triângulo Equilátero: possui os 3 lados iguais.
# 	Triângulo Isóscele: possui 2 lados iguais.
# 	Triângulo Escaleno: possui 3 lados diferentes.

medida1 = input ("Digite a primeira medida do lado do triangulo: ")
medida2 = input ("Digite a segunda medida do lado do triangulo: ")
medida3 = input ("Digite a terceira medida do lado do triangulo:: ")

medida1 = int (medida1)
medida2 = int (medida2)
medida3 = int (medida3)

if medida1 == medida2 and medida1 == medida3:
    print("Triângulo Equilátero")
elif medida1 == medida2 or medida1 == medida3 or medida2 == medida3:
    print ("Triângulo Isóscele")
else:
    print ("Triângulo Escaleno")         