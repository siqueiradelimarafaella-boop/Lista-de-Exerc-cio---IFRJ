# 3.	Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
# ACESSO PERMITIDO caso a senha seja válida. 
# ACESSO NEGADO caso a senha seja inválida.

senha_valida = "1234"
senha_usuario = input("Entre com a senha:")

if (senha_valida == senha_usuario) :
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO") 