# 9.	Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário não informará valores iguais.

valor1 = input ("Digite o primeiro valor: ")
valor2 = input ("Digite o segundo valor: ")
valor3 = input ("Digite o terceiro valor: ")

valor1 = int (valor1)
valor2 = int (valor2)
valor3 = int (valor3)

if valor1 == valor2 or valor1 == valor3 or valor3 == valor2:
    print ("Valores iguais, tente novamente!")
elif valor1 > valor2 and  valor1 > valor3:
    print("O primeiro valor é o maior: ", valor1)
elif valor2 > valor1 and  valor2 > valor3:
    print("O segundo valor é o maior: ", valor2)
else:
    print("O terceiro valor é o maior: ", valor3)    