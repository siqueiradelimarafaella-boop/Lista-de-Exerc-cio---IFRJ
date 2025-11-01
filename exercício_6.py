# 6.	Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes
# Fórmulas:
# -	para homens: (72.7 * Altura) – 58
# -	para mulheres: (62.1 * Altura) – 44.7
print("Calcule o seu peso ideal")

altura = input("Digite sua altura: ")
altura = float(altura)

pessoa = input ("Digite 1:feminino 2:masculino: ")
pessoa = int(pessoa)


if pessoa == 2:
    peso_ideal1 = (72.7 * altura) - (58.0)
    print ("Seu peso ideal é: ", peso_ideal1)
elif pessoa == 1:
    peso_ideal2 = (62.1 * altura) - (44.7)
    print("Seu peso ideal é: ", peso_ideal2)
else:
    print("Entrada de sexo inválida, tente novamente!")    
