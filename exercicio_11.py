# 11.	Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
# 	Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
# 	Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
# 	Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)

print("Que tipo de triangulo é, a partir dos seus angulos? ")
print("LEMBRE DE NÃO DIGITAR ANGULOS QUE A SOMA DÊ MENOS/MAIS DE 180 graus")
angulo1 = input ("Digite o primeiro angulo do triangulo: ")
angulo2 = input ("Digite o segundo angulo do triangulo: ")
angulo3 = input ("Digite o terceiro angulo do triangulo: ")

angulo1 = int (angulo1)
angulo2 = int (angulo2)
angulo3 = int (angulo3)

if angulo1 + angulo2 + angulo3 != 180:
    print("Não é triangulo")
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("É Triângulo Retângulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("É Triângulo Obtusângulo")
else:
    print("É Triângulo Acutângulo")          

