# 1.	Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.

primeiro = input("Insira o primeiro valor:") 
segundo = input("Insira o segundo valor:") 

if primeiro > segundo: 
    print("o primeiro valor é maior")
elif segundo > primeiro:
    print("o segundo valor é maior")
else:
    print("Os valores sao iguais")    