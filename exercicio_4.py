# 4.	As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

entrada = input("Quantas maças você quer comprar? ")
entrada = int(entrada)


if entrada < 12:
    valor_1 = (0.3 * entrada)
    print ("Sua compra deu: ", valor_1)
else: 
    valor_2 = (0.25 * entrada)
    print ("Sua compra deu: ", valor_2)     