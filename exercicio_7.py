# 7.	Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
# 	Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
# 	Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
# 	Se o número de lados for maior a 5 escrever POLÍGONO.

import math
x = 3
raiz = math.sqrt(x)



lado = input("Digite a quantidade de lados do seu polígono: ")
lado = int(lado)

if lado < 3:
    print ("Não é um polígono, vá estudar!")
elif lado == 3:
    print("Então vamos calcular a área!!!")
    medida = input("Digite a medida do lado em centímetros: ")    
    medida = float (medida)

    triangulo = ((raiz/4)*(medida**2))
    print("É um triangulo e sua área é de: ", triangulo)

elif lado == 4:
    print("Então vamos calcular a área!!!")
    medida = input("Digite a medida do lado em centímetros: ") 
    medida = float (medida)

    quadrado = (medida**2)
    print("É um quadrado e sua área é de: ", quadrado)

else:
    print("Então vamos calcular a área!!!")
    medida = input("Digite a medida do lado em centímetros: ")
    medida = float (medida)
     
    poligono = ((lado*(medida**2))/ (4* math.tan(math.pi/lado)))
    print ("É um polígono de", lado, "lados e sua área é:" , poligono)       
