
# 9 - Faça um algoritmo que receba um número e retorne a tabuada desse número.

cont = 0
num = int(input('Digite um número inteiro que deseja fazer a tabuada: '))
while cont <= 10:
    print(cont, '* {} = '.format(num), (cont * num))
    cont = cont + 1
else:
    print("Tabuada de", num, "calculada:")
