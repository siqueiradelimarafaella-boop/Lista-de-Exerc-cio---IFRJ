# 2.	Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

ano_nascimento = input ("Insira seu ano de nascimento: ")
ano_nascimento = int(ano_nascimento)
ano_atual = 2025
idade = ano_atual - ano_nascimento

if idade < 18: 
    print ("Voce ainda nao pode votar")
else: 
    print("Voce pode votar")   