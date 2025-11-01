# 8.	Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
# 	Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
# 	Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

import math
x = 3
raiz = math.sqrt(x)



lado = input("Digite a quantidade de lados do seu polígono: ")
lado = int(lado)

if lado < 3:
    print ("NÃO É UM POLÍGONO")
elif lado >= 5:
    print ("POLÍGONO NÃO IDENTIFICADO")

elif lado == 3:
    print("Então vamos calcular a área!!!")
    medida = input("Digite a medida do lado em centímetros: ")    
    medida = float (medida)

    triangulo = ((raiz/4)*(medida**2))
    print("É um triangulo e sua área é de: ", triangulo)

else:
    print("Então vamos calcular a área!!!")
    medida = input("Digite a medida do lado em centímetros: ") 
    medida = float (medida)

    quadrado = (medida**2)
    print("É um quadrado e sua área é de: ", quadrado)


