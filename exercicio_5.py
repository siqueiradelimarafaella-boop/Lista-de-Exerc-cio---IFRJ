# 5.	Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor_1 = input("Entre com o primeiro valor: ")
valor_2 = input("Entre com o segundo valor: ")
valor_3 = input("Entre com o terceiro valor: ")


valor_1 = int (valor_1)
valor_2 = int (valor_2)
valor_3 = int (valor_3)

if valor_1 == valor_2 or valor_2 == valor_3 or valor_1 == valor_3: 
    print("Você digitou entradas iguais, tente novamente!")
elif (valor_1 > valor_2) and (valor_2 > valor_3) and (valor_1 > valor_3)  :
     print("Em ordem crescente temos", valor_1, valor_2, valor_3)
elif (valor_2 > valor_1) and (valor_1 > valor_3) and (valor_2 > valor_3)  :
     print("Em ordem crescente temos", valor_2, valor_1, valor_3)
elif (valor_2 > valor_3) and (valor_3 > valor_1) and (valor_2 > valor_1)  :
     print("Em ordem crescente temos", valor_2, valor_3, valor_1)    
elif (valor_3 > valor_1) and (valor_1 > valor_2) and (valor_3 > valor_2)  :
     print("Em ordem crescente temos", valor_3, valor_1, valor_2) 
elif (valor_1 > valor_3) and (valor_3 > valor_2) and (valor_1 > valor_2)  :
     print("Em ordem crescente temos", valor_1, valor_3, valor_2) 
else: 
    print("Em ordem crescente temos", valor_3, valor_2, valor_1)    

 
